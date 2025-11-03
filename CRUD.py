import json
from datetime import datetime


def get_now_time():
    now = datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')
    return time

class Task_tracker:
    def __init__(self, filepath):
        print("初始化Task_tracker.")
        self.filepath = filepath
        print("尝试读取文件")
        try:
            with open(self.filepath, "r") as f:
                lines = [line for line in f]
        except FileNotFoundError:
                print("没有找到文件")
                lines = []
        if not lines:
            print("初始化文件中")
            text_defalt = Task_factory().create_from_des()
            self.Text = text_defalt # 当我需要的时候，将数据转化为Task类，使用类中的方法管理内容
            task_json = self.Text.get_json()
            with open(self.filepath, "w+") as f:
                f.write(task_json)
            print("文件初始化完成")

        print("Task_tracker初始化完成.")
        print("欢迎你的使用")

    def update(self):
        pass
    
    def add_task(self, task: "Task"):
        task_str = task.get_json()
        task_json = json.loads(task_str)
        result_id = self.search_id(id=task_json["id"])
        if result_id:
            print(f"id: {result_id} 已存在")
            print("分配新的id")
            id = self.get_new_id()
            print(id)
            task_json["id"] = id
            task_str = json.dumps(task_json)
        with open(self.filepath, "a") as f:
            f.write("\n" + task_str)

    def delete():
        pass

    def delete_id(self, id = None): # 通过读取全部数据，然后忽略对应id来实现删除。
        if id is None: # 如果没有传入id
            print("delete_id 操作需要传入 id")
            return
        
        if type(id) is int:
            id = str(id)
        # 读取文件
        with open(self.filepath, "r") as f:
            lines = [line.rstrip("\n") for line in f if line.strip() != ""]

        new_lines = []
        deleted = False

        for line in lines:
            task_dic = json.loads(line)
            print("是否删除：", task_dic)

            if task_dic["id"] == id:
                deleted = True
                print("删除")
                continue
            new_lines.append(line)

        with open(self.filepath, "w") as f:
            if new_lines:
                f.write("\n".join(new_lines))
            else:
                f.write("")

        if deleted:
            print(f"id : {id} has been deleted.")
        else:
            print(f"can't delete id : {id}")

    def search_id(self, id): # 如果找到，返回task的str，否则返回None
        if type(id) is int:
            id = str(id)

        with open(self.filepath, "r") as f:
            for task in f:
                try:
                    if task.strip() != "":
                        task_dic = json.loads(task)
                except json.decoder.JSONDecodeError:
                    print("json.decoder.JSONDecodeError")
                    continue
                if task_dic["id"] == id:
                    return task
        return None

    def get_new_id(self):
        with open(self.filepath, "r") as f:
            lines = [line for line in f if line.split != ""]
        ids = []
        for line in lines:
            line_json = json.loads(line)
            ids.append(line_json["id"])
        print(ids)
        id = 0
        while str(id) in ids:
            id += 1
        return str(id)

    def show_all(self):
        with open(self.filepath, "r") as f:
            for task in f:
                print(task)

    def save(self):
        text = self.Text.get_json()
        with open(self.filepath, "w") as f:
            f.write(text)
        print("save")


class Task:
    def __init__(
            self, 
            id = "0",
            description = "", 
            status = "todo",
        ):
        self.id = id
        self.description = description
        self.status = status
        now_time = get_now_time()
        self.createdAt = now_time
        self.updatedAt = now_time

    def get_json(self) -> str :
        txt_json = json.dumps(
            {
                "id" : self.id,
                "description" : self.description,   
                "status" : self.status,
                "createdAt" : self.createdAt,
                "updatedAt" : self.updatedAt,
            }
        )
        return txt_json
    
    def update_discription(self, disc):
        self.description = disc
        self.update_updatedAt()

    def update_updatedAt(self):
        self.updatedAt = get_now_time()

    def reset_createdAt(self, new_time):
        self.createdAt = new_time
    
    def update_status(self, new_status):
        self.status = new_status

    def reset_from_json(self, task_json):
        task_elements = json.loads(task_json)
        self.id = task_elements["id"]
        self.description = task_elements["description"]
        self.status = task_elements["status"]
        self.createdAt = task_elements["createdAt"]
        self.updatedAt = task_elements["updatedAt"]

class Task_factory:        
    def create_from_des(self, description = "Write any task here."):
        return Task(description = description)
    
    def create_from_json(self, task_json):
        task = Task()
        task.reset_from_json(task_json=task_json)
        return task
    

if __name__ == "__main__":
    FILEPATH = "json.txt"
    task_tracker = Task_tracker(FILEPATH)
    task_json = json.dumps({"id": "3", "description": "Write any task here.", "status": "todo", "createdAt": "2025-11-03 11:56:15", "updatedAt": "2025-11-03 11:56:15"})
    task = Task_factory().create_from_json(task_json=task_json)
    task_tracker.add_task(task)
    task_tracker.show_all()
    print("search id 1:", task_tracker.search_id(1))
    task_tracker.delete_id(id = 0)
    task_tracker.show_all()

    task_tracker.add_task(task=task)
    task_tracker.add_task(task=task)
    task_tracker.add_task(task=task)
