from PIL import Image,ExifTags
import os
import sys
import shutil
import hashlib

def uniq_pic(src_dir, dst_dir, start_file_idx):
    img_dict = {}
    for file_name in os.listdir(src_dir):
        file_path = os.path.join(src_dir,file_name)
        if not os.path.isfile(file_path):
            continue
        try :

            md5 = hashlib.md5(Image.open(file_path).tobytes()).hexdigest()
            print os.path.split(file_path)[1] + ' : ' + md5
#             exif = {
#                 ExifTags.TAGS[k]: v
#                 for k, v in img._getexif().items()
#                 if k in ExifTags.TAGS
#                 }
            if md5 in img_dict:
                print 'current name:' + file_path
                print 'prev name:' + img_dict[md5]
            else:
                img_dict [ md5 ] = file_path
        except Exception as e:
            print e
            continue
    file_idx = int(start_file_idx)
    for v in img_dict.values():
        print v
        print os.path.join(dst_dir,str(file_idx).zfill(4))+'.jpg'
        shutil.copy(v, os.path.join(dst_dir,str(file_idx).zfill(4))+'.jpg')
        file_idx = file_idx + 1

def main():
    if len(sys.argv) != 4:
        raise Exception("args length should be 4")
    uniq_pic(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    try:
        sys.exit(main())
    except  Exception as e:
        print e
        sys.exit(1)
