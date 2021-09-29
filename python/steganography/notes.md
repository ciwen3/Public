## create image from scratch 
https://code-maven.com/create-images-with-python-pil-pillow
```
from PIL import Image, ImageDraw
img = Image.new(mode, size, color)
img.save(filename)
```
## 60x30 pixel size
```
from PIL import Image
 
img = Image.new('RGB', (60, 30), color = 'red')
img.save('pil_red.png')
```
```
from PIL import Image
 
img = Image.new('RGB', (60, 30), color = (73, 109, 137))
img.save('pil_color.png')
```
## create image from scratch and add text
```
from PIL import Image, ImageDraw
 
img = Image.new('RGB', (100, 30), color = (73, 109, 137))
 
d = ImageDraw.Draw(img)
d.text((10,10), "Hello World", fill=(255,255,0))
 
img.save('pil_text.png')
```
```
from PIL import Image, ImageDraw, ImageFont
 
img = Image.new('RGB', (100, 30), color = (73, 109, 137))
 
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10,10), "Hello world", font=fnt, fill=(255, 255, 0))
 
img.save('pil_text_font.png')
```







```
img = Image.new('RGB', (width,height), "red")
```
```
from PIL import Image

img = Image.new('RGB', (300, 200), (228, 150, 150))
img.show()
```


https://auth0.com/blog/read-edit-exif-metadata-in-photos-with-python/
## check for exif data:
```
for index, image in enumerate(images):
    if image.has_exif:
        status = f"contains EXIF (version {image.exif_version}) information."
    else:
        status = "does not contain any EXIF information."
    print(f"Image {index} {status}")
```

## determine if two images have the same exif data
```
common_members = set(image_members[0]).intersection(set(image_members[1]))
common_members_sorted = sorted(list(common_members))
print("Image 0 and Image 1 have these members in common:")
print(f"{common_members_sorted}")
```

https://stackoverflow.com/questions/8770121/copying-and-writing-exif-information-from-one-image-to-another-using-pyexiv2
## copy exif from one picture to another
```
def get_exif(file):
    """
    Retrieves EXIF information from a image
    """
    ret = {}
    metadata = pyexiv2.ImageMetadata(str(file))
    metadata.read()
    info = metadata.exif_keys
    for key in info:
        data = metadata[key]
        ret[key] = data.raw_value
    return ret

def write_exif(originFile, destinationFile, **kwargs):
    """
    This function would write an exif information of an image file to another image file
    """

    exifInformation = get_exif(originFile)
    metadata = pyexiv2.ImageMetadata(str(destinationFile))
    for key, value in exifInformation.iteritems():
        metadata[key] = value

    try:
        metadata.write()
    except:
        return False
    else:
        return True
```

```
m1 = pyexiv2.ImageMetadata( source_filename )
m1.read()
# modify tags ...
# m1['Exif.Image.Key'] = pyexiv2.ExifTag('Exif.Image.Key', 'value')
m1.modified = True # not sure what this is good for
m2 = pyexiv2.metadata.ImageMetadata( destination_filename )
m2.read() # yes, we need to read the old stuff before we can overwrite it
m1.copy( m2 )
m2.write()
```

```
import pyexiv2
metadata = pyexiv2.ImageMetadata(image_name)
metadata.read() 
metadata.modified = True
metadata.writable = os.access(image_name ,os.W_OK)
metadata['Exif.Image.Copyright']  = pyexiv2.ExifTag('Exif.Image.Copyright', 'copyright@youtext') 
metadata.write()
```















https://stackoverflow.com/questions/400788/resize-image-in-python-without-losing-exif-data

```
import jpeg
jpeg.setExif(jpeg.getExif('foo.jpg'), 'foo-resized.jpg') 
```

```
image = Image.open('test.jpg')
exif = image.info['exif']
# Your picture process here
image = image.rotate(90)
image.save('test_rotated.jpg', 'JPEG', exif=exif)
```




