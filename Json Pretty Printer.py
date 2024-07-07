"""
{
  "id":"0001",
  "type":"donut",
  "name":"Cake",
  "ppu":0.55,
  "batters":{
    "batter":[
      {
        "id":"1001",
        "type":"Regular"
      },
      {
        "id":"1002",
        "type":"Chocolate"
      }
    ]
  },
  "topping":[
    {
      "id":"5001",
      "type":"None"
    },
    {
      "id":"5002",
      "type":"Glazed"
    }
  ]
}
"""


def JsonPrettyPrint(s: str) -> str:
    """'{[' add indentation to the following lines.
        
    """
    indent = 0
    res = []
    for c in s:
        if c.isspace():
            continue
        if c in '{[':
            indent += 1
        if c in "{[,":
            res.append(c)
            res.append('\n')
            res.append('\t' * indent)
        elif c in "}]":
            indent -= 1
            res.append('\n')
            res.append('\t' * indent)
            res.append(c)
        else:
            res.append(c)

    return "".join(res)


if __name__ == "__main__":
    print(
        JsonPrettyPrint(
            '{"id": "0001", "type": "donut","name": "Cake","ppu": 0.55, "batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" }]}'
        ))
