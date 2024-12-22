import json

# read json file
filename = 'output-1.json'
data = ""
with open(filename, 'r', encoding='utf-8') as f:
    data = json.load(f)

# remove title, header, footer
for item in data:
    if 'title' in item:
        del item['title']
    if 'html' in item:
        item['html'] = item['html'].replace(
            # header
            '關於單車節\n參加資訊\n主題活動\n知識論壇\n合作夥伴\n紀念品小舖\n即刻報名\n', ''
        ).replace(
            # footer
            '\n\n第17屆大學科系博覽會\n\n關於單車節\n\n　｜　\n\n參加資訊\n主題活動\n\n　｜　\n\n知識論壇\n合作夥伴\n\n　｜　\n\n紀念品小鋪', ''
        ).replace(
            # sidebar
            '科系手冊\n文學院\n理學院\n管理學院\n工學院\n電機資訊學院\n社會科學院\n規劃與設計學院\n生物科學與科技學院\n醫學院\n不分系', ''
        )

# write json file
filename = 'output-1-clean.json'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)