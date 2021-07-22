

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
