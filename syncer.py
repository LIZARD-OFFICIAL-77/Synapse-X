import multiprocessing
import scratchattach
import os





class Syncer:
    def __init__(self,session:scratchattach.Session,scratch_id: int):
        self.__scr_id = scratch_id
        self.__session = session
        self.__scr_events = scratchattach.CloudEvents(str(self.__scr_id))
        self.__tw_events = scratchattach.TwCloudEvents(project_id="Synapse_X",cloud_host="ws://127.0.0.1:9080/")
        self.__scr_conn = self.__session.connect_cloud(str(self.__scr_id))
        self.__tw_conn = scratchattach.TwCloudConnection(project_id="Synapse_X",cloud_host="ws://127.0.0.1:9080/")

        @self.__scr_events.event
        def on_set(event: scratchattach.TwCloudEvents.Event):
            self.__tw_conn.set_var(event.var,event.value)
        @self.__tw_events.event
        def on_set(event: scratchattach.CloudEvents.Event):
            self.__scr_conn.set_var(event.var,event.value)

    def start(self):
        self.tw_process = multiprocessing.Process(target=self.__tw_events.start)
        self.scr_process = multiprocessing.Process(target=self.__scr_events.start)
        self.tw_process.start()
        self.scr_process.start()

    def __del__(self):
        try:
            self.tw_process.kill()
            self.scr_process.kill()
        except:
            pass
        del self




