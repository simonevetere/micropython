import camera
import fpga
import time
import __camera
import ubinascii
import gc

__camera.wake()
fpga.write(0x1005, b'')

def read_strm(addr, total, chunk):
  buf = []
  todo = total
  while todo > 0:
    sz = chunk if todo > chunk else todo
    buf.extend(fpga.read(addr, sz))
    todo -= sz
  return buf


class Capture:
  def __init__(self, dev, dim, blksize):
    if len(dim) != 3:
      raise Exception('dim must be an array of [xres, yres, bpp]')

    self.addr = dev*256 + 5
    self.total = dim[0] * dim[1] * dim[2]
    self.chunk = (252//dim[2]) * dim[2]
    self.blksize = blksize * dim[2]
    self.pos = None

    if self.total % self.blksize != 0:
      raise Exception('blksize is incompatible with image dimensions')

  def __iter__(self):
    if self.pos != None:
      raise Exception('capture already consumed')
    self.pos = 0
    return self

  def __next__(self):
    if self.pos < self.total:
      buf = read_strm(self.addr, self.blksize, self.chunk)
      self.pos += len(buf)
      return buf
    raise StopIteration

def capture(dim, blksize, readout_id=0):
  """
  Captures a single image from the camera, of the give dimensions from
  the FB Readout configured for the given blksize.  The dimensions
  should be given as [xres, yres, bpp]
  """
  dev = 0x51
  addr = dev*256 + 4
  fpga.write(addr, b'')
  return Capture(dev, dim, blksize)

while True:
  cap = capture([64,64,3],128,1)
  time.sleep(0.5);
  print("============")
  for buf in cap:
    ubinascii.b2a_base64(str(buf))
    gc.collect()
  cap =  None