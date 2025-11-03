from CRUD import *
import shlex

FILEPATH = "json.txt"

def help():
    print(
        "程序具有以下命令：\n" \
        "help\t查看帮助\n" \
        "add <description>\t添加具有description的任务，注意使用\"\"引用以表示一个句子\n" \
        "delete <id>\t删除id的任务\n" \
        "show\t显示所有任务\n" \
        "search <id>\t搜索id的任务\n" \
        "quit\t退出程序\n"
    )

def main():
    print("Task_Tracker is running.")
    task_tracker = Task_tracker(FILEPATH)
    task_factory = Task_factory()
    while True:
        line = input("cmd> ")
        args = shlex.split(line)

        # 解析参数
        cmd = args[0].lower()

        if cmd in ("exit", "quit"):
            print("you are quit.")
            break
        elif cmd == "help":
            help()
        elif cmd == "add":
            print("you add")
            description = args[1]
            task = task_factory.create_from_des(description=description)
            task_tracker.add_task(task=task)

            print(f"success to add the task: \n {task.get_json()}")

        elif cmd == "show":
            task_tracker.show_all()
        elif cmd == "delete":
            task_tracker.delete_id(args[1])
            print(f"id: {id} be deleted")
        elif cmd == "search":
            print("you search")
        else:
            print(f"Unknow: {cmd}, input world 'help' for more infomation.")
if __name__ == "__main__":
    main()
