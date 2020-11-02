#coding:utf-8
import pandas as pd
from openpyxl.styles import Alignment

class FormartJson:
    def __init__(self):
        self.data = '''
        {
  "operators": {
    "a": [
      {
        "key": "等于",
        "value": "1",
        "tag": "SelectOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "不等于",
        "value": "2",
        "tag": "SelectOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "为空",
        "value": "5",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "不为空",
        "value": "6",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "全部",
        "value": "-1",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      }
    ],
    "b": [
      {
        "key": "自定义",
        "value": "1",
        "tag": "TimeSelectTwo",
        "items": null,
        "dataGroup": 1
      },
      {
        "key": "全部",
        "value": "-1",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "为空",
        "value": "37",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "不为空",
        "value": "38",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "昨天",
        "value": "2",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "今天",
        "value": "3",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "每年今天",
        "value": "70",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "明天",
        "value": "12",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "近7天",
        "value": "13",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "近30天",
        "value": "14",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "近60天",
        "value": "20",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "上周",
        "value": "4",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "每年上周",
        "value": "71",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "本周",
        "value": "5",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "每年本周",
        "value": "72",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "下周",
        "value": "6",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "每年下周",
        "value": "73",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "上月",
        "value": "7",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "每年上月",
        "value": "74",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "本月",
        "value": "8",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "每年本月",
        "value": "39",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "下月",
        "value": "9",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "每年下月",
        "value": "40",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "上季度",
        "value": "27",
        "tag": "None",
        "items": null,
        "dataGroup": 6
      },
      {
        "key": "每年上季度",
        "value": "75",
        "tag": "None",
        "items": null,
        "dataGroup": 6
      },
      {
        "key": "本季度",
        "value": "28",
        "tag": "None",
        "items": null,
        "dataGroup": 6
      },
      {
        "key": "每年本季度",
        "value": "76",
        "tag": "None",
        "items": null,
        "dataGroup": 6
      },
      {
        "key": "下季度",
        "value": "41",
        "tag": "None",
        "items": null,
        "dataGroup": 6
      },
      {
        "key": "每年下季度",
        "value": "77",
        "tag": "None",
        "items": null,
        "dataGroup": 6
      },
      {
        "key": "去年",
        "value": "10",
        "tag": "None",
        "items": null,
        "dataGroup": 7
      },
      {
        "key": "今年",
        "value": "11",
        "tag": "None",
        "items": null,
        "dataGroup": 7
      },
      {
        "key": "明年",
        "value": "49",
        "tag": "None",
        "items": null,
        "dataGroup": 7
      },
      {
        "key": "最近X天（含今天）",
        "value": "24",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近第X天",
        "value": "50",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X天前",
        "value": "25",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来X天（不含今天）",
        "value": "32",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来第X天",
        "value": "51",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X天后",
        "value": "52",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近X周（含本周）",
        "value": "53",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近第X周",
        "value": "54",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X周前",
        "value": "55",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来X周（不含本周）",
        "value": "33",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来第X周",
        "value": "56",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X周后",
        "value": "57",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近X月（含本月）",
        "value": "29",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近第X月",
        "value": "58",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X月前",
        "value": "42",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来X月（不含本月）",
        "value": "34",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来第X月",
        "value": "59",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X月后",
        "value": "43",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近X季（含本季）",
        "value": "44",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近第X季",
        "value": "60",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X季前",
        "value": "45",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来X季（不含本季）",
        "value": "35",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来第X季",
        "value": "61",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X季后",
        "value": "46",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近X年（含本年）",
        "value": "30",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近第X年",
        "value": "62",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X年前",
        "value": "47",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来X年（不含本年）",
        "value": "36",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来第X年",
        "value": "63",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X年后",
        "value": "48",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "等于",
        "value": "19",
        "tag": "TimeSelectConstant",
        "items": [
          {
            "key": "自定义",
            "value": "0",
            "tag": "TimeSelectOne",
            "items": null,
            "dataGroup": 6
          },
          {
            "key": "今天",
            "value": "3",
            "tag": "None",
            "items": null,
            "dataGroup": 1
          },
          {
            "key": "本周第一天",
            "value": "4",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本周最后一天",
            "value": "5",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本月第一天",
            "value": "6",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "本月最后一天",
            "value": "7",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上月第一天",
            "value": "20",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上月最后一天",
            "value": "21",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "本季度第一天",
            "value": "8",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "本季度最后一天",
            "value": "9",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "上季度第一天",
            "value": "22",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "上季度最后一天",
            "value": "23",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "本年第一天",
            "value": "10",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "本年最后一天",
            "value": "11",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "上年第一天",
            "value": "24",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "上年最后一天",
            "value": "25",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          }
        ],
        "dataGroup": 0
      },
      {
        "key": "大于",
        "value": "15",
        "tag": "TimeSelectConstant",
        "items": [
          {
            "key": "自定义",
            "value": "0",
            "tag": "TimeSelectOne",
            "items": null,
            "dataGroup": 6
          },
          {
            "key": "今天",
            "value": "3",
            "tag": "None",
            "items": null,
            "dataGroup": 1
          },
          {
            "key": "本周第一天",
            "value": "4",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本周最后一天",
            "value": "5",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本月第一天",
            "value": "6",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "本月最后一天",
            "value": "7",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上月第一天",
            "value": "20",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上月最后一天",
            "value": "21",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "本季度第一天",
            "value": "8",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "本季度最后一天",
            "value": "9",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "上季度第一天",
            "value": "22",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "上季度最后一天",
            "value": "23",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "本年第一天",
            "value": "10",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "本年最后一天",
            "value": "11",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "上年第一天",
            "value": "24",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "上年最后一天",
            "value": "25",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          }
        ],
        "dataGroup": 0
      },
      {
        "key": "大于等于",
        "value": "17",
        "tag": "TimeSelectConstant",
        "items": [
          {
            "key": "自定义",
            "value": "0",
            "tag": "TimeSelectOne",
            "items": null,
            "dataGroup": 6
          },
          {
            "key": "今天",
            "value": "3",
            "tag": "None",
            "items": null,
            "dataGroup": 1
          },
          {
            "key": "本周第一天",
            "value": "4",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本周最后一天",
            "value": "5",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本月第一天",
            "value": "6",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "本月最后一天",
            "value": "7",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上月第一天",
            "value": "20",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上月最后一天",
            "value": "21",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "本季度第一天",
            "value": "8",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "本季度最后一天",
            "value": "9",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "上季度第一天",
            "value": "22",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "上季度最后一天",
            "value": "23",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "本年第一天",
            "value": "10",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "本年最后一天",
            "value": "11",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "上年第一天",
            "value": "24",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "上年最后一天",
            "value": "25",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          }
        ],
        "dataGroup": 0
      },
      {
        "key": "小于",
        "value": "16",
        "tag": "TimeSelectConstant",
        "items": [
          {
            "key": "自定义",
            "value": "0",
            "tag": "TimeSelectOne",
            "items": null,
            "dataGroup": 6
          },
          {
            "key": "今天",
            "value": "3",
            "tag": "None",
            "items": null,
            "dataGroup": 1
          },
          {
            "key": "本周第一天",
            "value": "4",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本周最后一天",
            "value": "5",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本月第一天",
            "value": "6",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "本月最后一天",
            "value": "7",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上月第一天",
            "value": "20",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上月最后一天",
            "value": "21",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "本季度第一天",
            "value": "8",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "本季度最后一天",
            "value": "9",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "上季度第一天",
            "value": "22",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "上季度最后一天",
            "value": "23",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "本年第一天",
            "value": "10",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "本年最后一天",
            "value": "11",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "上年第一天",
            "value": "24",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "上年最后一天",
            "value": "25",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          }
        ],
        "dataGroup": 0
      },
      {
        "key": "小于等于",
        "value": "18",
        "tag": "TimeSelectConstant",
        "items": [
          {
            "key": "自定义",
            "value": "0",
            "tag": "TimeSelectOne",
            "items": null,
            "dataGroup": 6
          },
          {
            "key": "今天",
            "value": "3",
            "tag": "None",
            "items": null,
            "dataGroup": 1
          },
          {
            "key": "本周第一天",
            "value": "4",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本周最后一天",
            "value": "5",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本月第一天",
            "value": "6",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "本月最后一天",
            "value": "7",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上月第一天",
            "value": "20",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上月最后一天",
            "value": "21",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "本季度第一天",
            "value": "8",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "本季度最后一天",
            "value": "9",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "上季度第一天",
            "value": "22",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "上季度最后一天",
            "value": "23",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "本年第一天",
            "value": "10",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "本年最后一天",
            "value": "11",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "上年第一天",
            "value": "24",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          },
          {
            "key": "上年最后一天",
            "value": "25",
            "tag": "None",
            "items": null,
            "dataGroup": 5
          }
        ],
        "dataGroup": 0
      },
      {
        "key": "最新X条",
        "value": "31",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      }
    ],
    "c": [
      {
        "key": "等于",
        "value": "1",
        "tag": "TextInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "不等于",
        "value": "2",
        "tag": "TextInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "开头是",
        "value": "7",
        "tag": "TextInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "结尾是",
        "value": "8",
        "tag": "TextInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "包含",
        "value": "3",
        "tag": "TextInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "不包含",
        "value": "4",
        "tag": "TextInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "为空",
        "value": "5",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "不为空",
        "value": "6",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "全部",
        "value": "-1",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      }
    ],
    "d": [
      {
        "key": "等于",
        "value": "1",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "不等于",
        "value": "2",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "大于",
        "value": "3",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "小于",
        "value": "4",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "大于等于",
        "value": "5",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "小于等于",
        "value": "6",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "介于",
        "value": "9",
        "tag": "DigitInputTwo",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "为空",
        "value": "7",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "不为空",
        "value": "10",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "全部",
        "value": "-1",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      }
    ],
    "e": [
      {
        "key": "等于",
        "value": "1",
        "tag": "SelectOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "为空",
        "value": "2",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "不为空",
        "value": "3",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "全部",
        "value": "-1",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      }
    ],
    "f": [
      {
        "key": "等于",
        "value": "1",
        "tag": "SelectOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "不等于",
        "value": "2",
        "tag": "SelectOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "当前用户",
        "value": "3",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "非当前用户",
        "value": "4",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "为空",
        "value": "5",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "不为空",
        "value": "6",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "全部",
        "value": "-1",
        "tag": "None",
        "items": null,
        "dataGroup": 0
      }
    ],
    "g": [
      {
        "key": "自定义",
        "value": "1",
        "tag": "TimeSelectTwo",
        "items": null,
        "dataGroup": 1
      },
      {
        "key": "全部",
        "value": "-1",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "为空",
        "value": "37",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "不为空",
        "value": "38",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "上月",
        "value": "7",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "本月",
        "value": "8",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "每年本月",
        "value": "39",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "下月",
        "value": "9",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "每年下月",
        "value": "40",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "上季度",
        "value": "27",
        "tag": "None",
        "items": null,
        "dataGroup": 6
      },
      {
        "key": "本季度",
        "value": "28",
        "tag": "None",
        "items": null,
        "dataGroup": 6
      },
      {
        "key": "下季度",
        "value": "41",
        "tag": "None",
        "items": null,
        "dataGroup": 6
      },
      {
        "key": "去年",
        "value": "10",
        "tag": "None",
        "items": null,
        "dataGroup": 7
      },
      {
        "key": "今年",
        "value": "11",
        "tag": "None",
        "items": null,
        "dataGroup": 7
      },
      {
        "key": "明年",
        "value": "49",
        "tag": "None",
        "items": null,
        "dataGroup": 7
      },
      {
        "key": "最近X月（含本月）",
        "value": "29",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X月前",
        "value": "42",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来X月（不含本月）",
        "value": "34",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X月后",
        "value": "43",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近X季（含本季）",
        "value": "44",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X季前",
        "value": "45",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来X季（不含本季）",
        "value": "35",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X季后",
        "value": "46",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "最近X年（含本年）",
        "value": "30",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X年前",
        "value": "47",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "未来X年（不含本年）",
        "value": "36",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "X年后",
        "value": "48",
        "tag": "DigitInputOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "等于",
        "value": "19",
        "tag": "TimeSelectConstant",
        "items": [
          {
            "key": "自定义",
            "value": "0",
            "tag": "TimeSelectOne",
            "items": null,
            "dataGroup": 1
          },
          {
            "key": "本月",
            "value": "12",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "上月",
            "value": "13",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "下月",
            "value": "14",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本季度",
            "value": "15",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上季度",
            "value": "16",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "下季度",
            "value": "17",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "今年",
            "value": "18",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "去年",
            "value": "19",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "明年",
            "value": "26",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          }
        ],
        "dataGroup": 0
      },
      {
        "key": "大于",
        "value": "15",
        "tag": "TimeSelectConstant",
        "items": [
          {
            "key": "自定义",
            "value": "0",
            "tag": "TimeSelectOne",
            "items": null,
            "dataGroup": 1
          },
          {
            "key": "本月",
            "value": "12",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "上月",
            "value": "13",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "下月",
            "value": "14",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本季度",
            "value": "15",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上季度",
            "value": "16",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "下季度",
            "value": "17",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "今年",
            "value": "18",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "去年",
            "value": "19",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "明年",
            "value": "26",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          }
        ],
        "dataGroup": 0
      },
      {
        "key": "小于",
        "value": "16",
        "tag": "TimeSelectConstant",
        "items": [
          {
            "key": "自定义",
            "value": "0",
            "tag": "TimeSelectOne",
            "items": null,
            "dataGroup": 1
          },
          {
            "key": "本月",
            "value": "12",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "上月",
            "value": "13",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "下月",
            "value": "14",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本季度",
            "value": "15",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上季度",
            "value": "16",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "下季度",
            "value": "17",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "今年",
            "value": "18",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "去年",
            "value": "19",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "明年",
            "value": "26",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          }
        ],
        "dataGroup": 0
      },
      {
        "key": "大于等于",
        "value": "17",
        "tag": "TimeSelectConstant",
        "items": [
          {
            "key": "自定义",
            "value": "0",
            "tag": "TimeSelectOne",
            "items": null,
            "dataGroup": 1
          },
          {
            "key": "本月",
            "value": "12",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "上月",
            "value": "13",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "下月",
            "value": "14",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本季度",
            "value": "15",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上季度",
            "value": "16",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "下季度",
            "value": "17",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "今年",
            "value": "18",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "去年",
            "value": "19",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "明年",
            "value": "26",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          }
        ],
        "dataGroup": 0
      },
      {
        "key": "小于等于",
        "value": "18",
        "tag": "TimeSelectConstant",
        "items": [
          {
            "key": "自定义",
            "value": "0",
            "tag": "TimeSelectOne",
            "items": null,
            "dataGroup": 1
          },
          {
            "key": "本月",
            "value": "12",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "上月",
            "value": "13",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "下月",
            "value": "14",
            "tag": "None",
            "items": null,
            "dataGroup": 2
          },
          {
            "key": "本季度",
            "value": "15",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "上季度",
            "value": "16",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "下季度",
            "value": "17",
            "tag": "None",
            "items": null,
            "dataGroup": 3
          },
          {
            "key": "今年",
            "value": "18",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "去年",
            "value": "19",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          },
          {
            "key": "明年",
            "value": "26",
            "tag": "None",
            "items": null,
            "dataGroup": 4
          }
        ],
        "dataGroup": 0
      }
    ],
    "g_SelectConstant": [
      {
        "key": "自定义",
        "value": "0",
        "tag": "TimeSelectOne",
        "items": null,
        "dataGroup": 1
      },
      {
        "key": "本月",
        "value": "12",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "上月",
        "value": "13",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "下月",
        "value": "14",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "本季度",
        "value": "15",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "上季度",
        "value": "16",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "下季度",
        "value": "17",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "今年",
        "value": "18",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "去年",
        "value": "19",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "明年",
        "value": "26",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      }
    ],
    "h": [
      {
        "key": "自定义",
        "value": "1",
        "tag": "TimeSelectTwo",
        "items": null,
        "dataGroup": 1
      },
      {
        "key": "全部",
        "value": "-1",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "为空",
        "value": "37",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "不为空",
        "value": "38",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "等于",
        "value": "19",
        "tag": "TimeSelectConstant",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "大于",
        "value": "15",
        "tag": "TimeSelectConstant",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "小于",
        "value": "16",
        "tag": "TimeSelectConstant",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "大于等于",
        "value": "17",
        "tag": "TimeSelectConstant",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "小于等于",
        "value": "18",
        "tag": "TimeSelectConstant",
        "items": null,
        "dataGroup": 0
      }
    ],
    "i": [
      {
        "key": "自定义",
        "value": "1",
        "tag": "TimeSelectOne",
        "items": null,
        "dataGroup": 0
      },
      {
        "key": "全部",
        "value": "-1",
        "tag": "None",
        "items": null,
        "dataGroup": 1
      },
      {
        "key": "昨天",
        "value": "2",
        "tag": "None",
        "items": null,
        "dataGroup": 1
      },
      {
        "key": "今天",
        "value": "3",
        "tag": "None",
        "items": null,
        "dataGroup": 1
      },
      {
        "key": "明天",
        "value": "12",
        "tag": "None",
        "items": null,
        "dataGroup": 1
      },
      {
        "key": "本周第一天",
        "value": "4",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "本周最后一天",
        "value": "5",
        "tag": "None",
        "items": null,
        "dataGroup": 2
      },
      {
        "key": "本月第一天",
        "value": "6",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "本月最后一天",
        "value": "7",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "上月第一天",
        "value": "20",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "上月最后一天",
        "value": "21",
        "tag": "None",
        "items": null,
        "dataGroup": 3
      },
      {
        "key": "本季度第一天",
        "value": "8",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "本季度最后一天",
        "value": "9",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "上季度第一天",
        "value": "22",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "上季度最后一天",
        "value": "23",
        "tag": "None",
        "items": null,
        "dataGroup": 4
      },
      {
        "key": "本年第一天",
        "value": "10",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "本年最后一天",
        "value": "11",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "上年第一天",
        "value": "24",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      },
      {
        "key": "上年最后一天",
        "value": "25",
        "tag": "None",
        "items": null,
        "dataGroup": 5
      }
    ]
  },
  "code": null
}'''

        self.data = str(self.data).replace('null','"null"')
        self.klass ={"a":"选项字段","b":'日期字段',"c":"文本字段","d":"数字字段","e":"等于字段","f":"当前用户","g":"年月","h":"时分","i":"单日期类型"}
        self.read()
        self.write_excel()
    def read(self):
        self.pd_data = pd.read_json(self.data, orient='records')
        self.pd_data = self.pd_data['operators']


    def write_excel(self):
        rowName = self.pd_data._stat_axis.values;
        print(self.pd_data.values)

        with pd.ExcelWriter('/Users/amanda/Downloads/operator.xlsx') as writer:
            all = []
            for key in rowName:

                sheet_name = key
                if key in self.klass:
                    print(self.klass[key])
                    sheet_name = key + r'（%s）' % self.klass[key]

                r = pd.DataFrame(self.pd_data[key])
                r.to_excel(writer, sheet_name= sheet_name,header=sheet_name)
                ws = writer.sheets[sheet_name]
                ws.insert_rows(1)
                ws.merge_cells('A1:F1')
                ws.cell(column=1, row=1, value=sheet_name).alignment = Alignment(horizontal='center', vertical='center')
                ws.column_dimensions['B'].width = 15

                writer.save()

                all.extend(self.pd_data[key])

            sd = pd.DataFrame(all)
            sd = sd.drop_duplicates(subset='key')
            sd.to_excel(writer, sheet_name='all')


FormartJson()