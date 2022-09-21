import ueberzug.lib.v0 as ueberzug
import threading
from plantuml import PlantUML
import time

class NvimPlantUML:
    def __init__(self, path, out_path):
        #thread = threading.Thread(target=self.callback)
        self.out_path = out_path
        self.plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
        self.plantuml.processes_file(path, outfile=out_path)

    def callback(self):
        return
    

    def draw(self):
        with ueberzug.Canvas() as c:
            demo = c.create_placement('demo', x=0, y=0, scaler=ueberzug.ScalerOption.COVER.value)
            demo.path = self.out_path
            demo.visibility = ueberzug.Visibility.VISIBLE

            with c.synchronous_lazy_drawing:
                demo.x = 50
                demo.y = 0
                demo.path = self.out_path
            while True:
                time.sleep(0.1)


if __name__ == '__main__':
    path = './sample.pu'
    out_path = './sample.png'
    nvim_pu = NvimPlantUML(path, out_path)
    nvim_pu.draw()
