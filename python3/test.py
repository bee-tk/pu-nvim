import ueberzug.lib.v0 as ueberzug
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
import threading
from plantuml import PlantUML
import time
from multiprocessing import Process

class NvimPlantUML(PatternMatchingEventHandler):
    def __init__(self, path, out_path):
        self.path = path
        self.out_path = out_path
        self.plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
        self.plantuml.processes_file(path, outfile=out_path)

        # file change handler
        super(NvimPlantUML, self).__init__(patterns=['*.pu'])
        self.observer = Observer()
        self.observer.schedule(self, './', recursive=True)

        self.modified = False

        p = Process(target=self.draw, args=())
        p.start()

    def on_modified(self, event):
        self.modified = True
    
    def draw(self):
        self.observer.start()
        with ueberzug.Canvas() as c:
            demo = c.create_placement('demo', x=50, y=0, scaler=ueberzug.ScalerOption.COVER.value)
            demo.path = self.out_path
            demo.visibility = ueberzug.Visibility.VISIBLE
            result = None

            while True:
                mode = vim.command_output('echo mode()')
                if mode == 'n':
                    if self.modified:
                        # .pu -> .png
                        result = self.plantuml.processes_file(self.path, outfile=self.out_path)
                        self.modified = False
                    visualize = ueberzug.Visibility.VISIBLE

                    # failed plantuml process
                    if result == False:
                        break
                elif mode == 'i':
                    visualize = ueberzug.Visibility.INVISIBLE

                with c.synchronous_lazy_drawing:
                    demo.x = 50
                    demo.y = 0
                    demo.path = self.out_path
                    demo.visibility = visualize 
                time.sleep(0.3)

def test():
    #print(mode)
    path = './sample.pu'
    out_path = './sample.png'
    nvim_pu = NvimPlantUML(path, out_path)
