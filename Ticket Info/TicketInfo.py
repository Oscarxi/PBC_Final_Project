import pandas as pd
from pyparsing import col

column = ["影城", "票價"]
info = [
    # 國賓：西門、長春、林口、新莊、淡水
    ["西門國賓鉅院", "400"],
    ["西門國賓2、3廳", "310"],
    ["長春國賓", "320"],
    ["林口國賓", "290"],
    ["新莊國賓", "300"],
    ["淡水國賓", "290"],
    # 秀泰：欣欣、今日、東南亞、板橋、樹林、土城
    ["欣欣秀泰", "290"],
    ["今日秀泰", "280"],
    ["東南亞秀泰", "280"],
    ["板橋秀泰", "290"],
    ["樹林秀泰", "290"],
    ["土城秀泰", "290"],
    # 光點：台北、華山
    ["台北光點", "260"],
    ["華山光點", "270"],
    # 美麗華大直
    ["美麗華大直", "330"],
    # 新光：台北、天母
    ["台北新光", "280"],
    ["天母新光", "310"],
    # in89
    ["in89", "300"],
    # 樂聲
    ["樂聲", "280"],
    # 真善美
    ["真善美", "270"],
    # 喜滿客絕色
    ["西門絕色", "270"],
    # 威秀：信義、板橋大遠百、京站、松仁、中和環球、林口
    ["信義威秀", "340"],
    ["板橋大遠百威秀", "330"],
    ["京站威秀", "340"],
    ["松仁威秀" , "370"],
    ["中和環球威秀", "310"],
    ["林口威秀", "300"],
    # 總督
    ["總督", "270"],
    # 哈拉
    ["哈拉", "290"],
    # 百老匯
    ["百老匯", "280"],
    # 梅花
    ["梅花", "270"],
    # 新民生
    ["新民生", "260"],
    # 誠品
    ["誠品","290"],
    # 喜樂時代：南港、永和
    ["南港喜樂時代", "310"],
    ["永和喜樂時代", "300"],
    # 美麗新：皇家、淡海、宏匯
    ["皇家", "650"],
    ["美麗新淡海", "290"],
    ["美麗新宏匯", "300"],
    # 鴻金寶麻吉
    ["鴻金寶麻吉", "260"],
    # 三重天台
    ["三重天台", "270"]
    ]

ticketInfo = pd.DataFrame(info, columns = column)
ticketInfo.to_csv("票價資訊.csv")

print("finished")