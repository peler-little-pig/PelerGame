## 概述

PelerGame 提供了基于面向对象，继承多态的设计模式。这使得您可以非常方便的添加枪械，子弹。

## 自定义子弹
在项目的 `Egg` 文件夹下新建 Python 文件，内容如下：

```python
# 引入模块
from Egg.BaseEgg import *

class 子弹名称(BaseEgg):
    def __init__(self, left: float, top: float, width: float, height: float, x, y, whose):
        super().__init__(left, top, width, height, x, y, whose, 子弹图片路径（str类型）, 子弹速度（int类型）, 子弹伤害（int类型）)
```

例子：
```python
from Egg.BaseEgg import *

class GunEgg(BaseEgg):
    def __init__(self, left: float, top: float, width: float, height: float, x, y, whose):
        super().__init__(left, top, width, height, x, y, whose, './Res/Picture/image/egg/egg.png', 10, 3)

```

## 自定义枪械
在项目的 `Thing` 文件夹下新建 Python 文件，内容如下：

```python
# 引入模块
from Thing.BaseThing import *   # 必须引入
from Egg.HandGunEgg import *   # 根据子弹引入

class 枪械名称(BaseThing):
    def __init__(self, left: float, top: float):
        super().__init__(
            left=left,
            top=top,
            width=枪械图片宽度（int类型）,
            height=枪械图片高度（int类型）,
            rotate_point=枪械旋转点（tuple类型，如(17,16)）,
            length=枪械枪身长度（int类型）,
            WAIT=枪械射击间隔（int类型）,
            image_path=枪械图片路径（str类型）,
            cost=枪械消耗能量（int类型）,
            egg_type=枪械所用子弹（继承于 BaseEgg 的类）,
            name=枪械名称（str类型）)
```

例子：

```python
from Egg.NoneEgg import NoneEgg
from Thing.BaseThing import *

class BloodDrinkThing(BaseThing):
    def __init__(self, left: float, top: float):
        super().__init__(
            left=left,
            top=top,
            width=30,
            height=30,
            rotate_point=(5, 15),
            length=30,
            WAIT=0,
            image_path='./Res/Picture/image/drink/blood.png',
            cost=0,
            egg_type=NoneEgg,
            name='生命药水')
```

当枪械是物品时，如生命药水，您不希望其发射子弹，则可以将子弹定义为 `NoneEgg`。

### 将枪械加入到宝箱列表
将枪械加入到宝箱列表后，即有机会在武器宝箱中出现。

修改 项目的 `Thing` 文件夹中的 `ThingList.py`：

```
from Thing.GunThing import *
from Thing.HandGunThing import *
# 在此处引入你要添加的枪械

thing_list = [
    GunThing,
    HandGunThing,
    要添加的枪械的类的名称,
    ...
]
```
