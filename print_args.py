import argparse

class Config():

    def __init__(self):
        pass

    def parse(self):
        parser = argparse.ArgumentParser(description='GAN generation')
        parser.add_argument('--inpFile_ja', default='demo_ja/demo.txt', type=str)
        parser.add_argument('--inpImages_ja', default='dataset_ja/images', type=str)
        parser.add_argument('--inpClothMask_ja', default='dataset_ja/cloth_mask', type=str)
        parser.add_argument('--inpClothImage_ja', default='dataset_ja/cloth_image', type=str)
        parser.add_argument('--inpParseChip_ja', default='dataset_ja/parse_cihp', type=str)
        parser.add_argument('--inpPoseCoco_ja', default='dataset_ja/pose_coco', type=str)

        args = parser.parse_args()
        #print("args")
        return args
        

if __name__ == "__main__":
    pass
