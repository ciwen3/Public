

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



