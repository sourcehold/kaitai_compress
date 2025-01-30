import dclimplode

class DCL(object):
  def decode(self, data):
    o = dclimplode.decompressobj
    return o.decompress(data)
  
  def encode(self, data):
    o = dclimplode.compressobj(data) + o.flush()
    return o.compress()
    
