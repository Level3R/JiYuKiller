#SPDX-License-Identifier: MIT
#Copyright © 2025 Lv3R
from PySimpleGUI import PySimpleGUI as sg
from concurrent.futures import ThreadPoolExecutor
import subprocess
import sys
import os
import time
from windows_api.admin import is_admin, get_admin
version = "V1.2.0"
sg.theme("Default1")
if not is_admin():
    get_admin()
sg.Popup("免责声明：使用本程序所导致的任何后果皆由使用者自行承担，开发者不负任何责任。", title="免责声明", custom_text=("我已知晓且同意该声明"), grab_anywhere=True)
def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None
file_path = find_file("StudentMain.exe", r"C:\Program Files (x86)\mythware")
if file_path == None:
    file_path = find_file("StudentMain.exe", r"C:\Program Files\mythware")
    if file_path == None:
        file_path = find_file("StudentMain.exe", r"D:\Program Files (x86)\mythware")
        if file_path == None:
            file_path = find_file("StudentMain.exe", r"D:\Program Files\mythware")
            if file_path == None:
                file_path = ""
executor = ThreadPoolExecutor(max_workers=1)
ps_command0 = r"""
$process0 = Get-Process -Name StudentMain -ErrorAction SilentlyContinue
if ($process0) {
    Stop-Process -Name StudentMain -Force
    "杀死极域成功"
}
else {
    "极域未运行"
}
"""
ps_command1 = fr"""
$process1 = Start-Process "{file_path}"
"""
def output(text):
    list.append(str(text))
    window["-LB-"].update(values=list)
    if len(list) > 5:
                window["-LB-"].update(scroll_to_index=len(list)-5)
def Kill():
    result = subprocess.run(
        ["powershell", "-Command", ps_command0],
        capture_output=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
        text=True
    )
    list.append(result.stdout)
    window["-LB-"].update(values=list)
    if len(list) > 5:
        window["-LB-"].update(scroll_to_index=len(list)-5)
list = []
futures = []
layout0 = [
    [sg.LB(list, size=(85, 5), default_values=None, key="-LB-", enable_events=False, bind_return_key=False, select_mode=None)]
]
layout=[
    [sg.T("注意，您正在使用本程序的预发布版本，部分功能可能无法正常使用。", text_color="red")],
    [sg.B("KILL(Space)", key="-KILL-", button_color="red",tooltip="KILL：杀死极域并使其不能自启动；停止：停止杀死极域"), sg.B("恢复(Enter)", key="-RESTART-", button_color="green",tooltip="恢复极域运行", bind_return_key=True), sg.B("清空输出", key="-CLEAN-",tooltip="清空输出列表的全部内容"), sg.B("开启置顶", key="-TOP-",tooltip="窗口将强制置顶"), sg.B("关闭置顶", key="-UNTOP-",tooltip="窗口将不再强制置顶"), sg.B("退出(Alt+F4)", key="-EXIT-", button_color="green", tooltip="退出程序"), sg.T(f"{version}"+" By Lv3R", key="-INFO-", enable_events=True, text_color="blue", tooltip="更多信息") , sg.In("", key="-FILEPATH-", visible=False)],[sg.Fr(title="输出", layout=layout0)],
    [sg.T("免责声明：使用本程序所导致的任何后果皆由使用者自行承担，开发者不负任何责任。"), sg.FileBrowse("定位",key="-POSITION-", file_types=(("EXE", "StudentMain.exe"), ), target="-FILEPATH-", tooltip="手动定位极域")]
]
window=sg.Window("JiYuKiller", layout, keep_on_top=True, resizable=True, grab_anywhere=True, finalize = True)
force_topmost = True
kill = False
TIMEOUT_TOP = 500
TIMEOUT_KILL = 1000
last_top_time = 0
last_kill_time = 0
list.append("已开启置顶")
window["-LB-"].update(values=list)
while True:
    current_time = time.time() * 1000
    timeout = min(
        max(TIMEOUT_TOP - (current_time - last_top_time), 0),
        max(TIMEOUT_KILL - (current_time - last_kill_time), 0)
    )
    event, values=window.read(timeout=int(timeout))
    if (event is None) or (event == "-EXIT-"):
        window.close()
        for future in futures:
            if not future.running():
                future.cancel()
        executor.shutdown(wait=False)
        sys.exit(0)
    if event == "-KILL-":
        if window["-KILL-"].ButtonColor == ("1234567890", "red"):
            kill = True
            window["-KILL-"].update(button_color="yellow", text="停止(Space)")
            output("开始杀死极域")
        elif window["-KILL-"].ButtonColor == ("1234567890", "yellow"):
            kill = False
            window["-KILL-"].update(button_color="red", text="KILL(Space)")
            output("已停止杀死极域")
    elif event == "-RESTART-":
        kill = False
        if file_path != "":
            window["-POSITION-"].update(visible=False)
            window["-KILL-"].update(button_color="red", text="KILL(Space)")
            result = subprocess.run(
                ["powershell", "-Command", ps_command1],
                capture_output=True,
                creationflags=subprocess.CREATE_NO_WINDOW,
                text=True
            )
            output("已尝试恢复极域")
        else:
            if values["-FILEPATH-"] != "":
                file_path = values["-FILEPATH-"]
                window["-POSITION-"].update(visible=False)
                window["-KILL-"].update(button_color="red", text="KILL(Space)")
                result = subprocess.run(
                    ["powershell", "-Command", ps_command1],
                    capture_output=True,
                    creationflags=subprocess.CREATE_NO_WINDOW,
                    text=True
                )
                window["-POSITION-"].update(visible=True)
                output("已尝试恢复极域")
            else:
                window["-KILL-"].update(button_color="red", text="KILL(Space)")
                output("未找到极域，请点击“定位”手动定位")
    if event == "-CLEAN-":
        list = []
        window["-LB-"].update(values=list)
    if event == "-TOP-":
        force_topmost = True
        window.TKroot.attributes("-topmost", 1)
        output("已开启置顶")
    elif event == "-UNTOP-":
        force_topmost = False
        window.TKroot.attributes("-topmost", 0)
        output("已关闭置顶")
    if event == "-INFO-":
        sg.Popup("JiYuKiller", f"版本：{version}","作者：Lv3R",  "问题反馈：lv3r@qq.com", "更新日志：", "    新增 手动定位极域功能", "    优化 输出内容", "    优化 代码结构", "    修复 退出 JiYuKiller 时耗时长甚至未响应的问题", "开源：", "    本项目已在 GitHub 开源，遵循 MIT 协议", "特别鸣谢：", "    梦鱼大佬，本程序的开发灵感来源于他开发的 JiYuTrainer", title="更多信息", custom_text=(" 确定 "), non_blocking=True, grab_anywhere=True, image=b"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")
    if event == sg.TIMEOUT_EVENT:
        if force_topmost and (current_time - last_top_time >= TIMEOUT_TOP):
            window.TKroot.attributes("-topmost", 1)
            window.bring_to_front()
            last_top_time = current_time
        if kill and (current_time - last_kill_time >= TIMEOUT_KILL):
            future = executor.submit(Kill)
            futures.append(future)
            last_kill_time = current_time