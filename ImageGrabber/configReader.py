import json


class configReader:
    PATH = 'ImageGrabber/config.json'

    def __init__(self) -> None:
        self.config = {}
        self.load()
        
        self.path:str = self.config['path']
        self.cameras:list[dict] = self.config['cameras']
        self.train_id = self.config['train_id']
        self.max_file_count = int(self.config['max_file_count'])
        self.output_type = self.config['output']
        self.video_frames_count = int(self.config['video_frames'])
        self.video_fps = int(self.config['video_fps'])
        self.motion = self.config['motion'].lower() == 'true'
        self.motion_sens = int(self.config['motion_sens'])


    def load(self,):
        with open(self.PATH) as f:
            self.config = json.load(f)
        

configReader()