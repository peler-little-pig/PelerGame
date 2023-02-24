## 项目文件树

```
.
├── Actor
│   ├── BadActor
│   │   ├── BaseBadActor.py
│   │   ├── __init__.py
│   ├── BaseActor.py
│   ├── GoodActor
│   │   ├── BaseGoodActor.py
│   │   ├── __init__.py
│   ├── HireActor
│   │   ├── BaseHireActor.py
│   │   ├── __init__.py
│   ├── __init__.py
│   └── SellActor
│       ├── BaseSellActor.py
│       ├── __init__.py
├── BetterPygame
│   ├── Function.py
│   ├── __init__.py
│   ├── Rect.py
│   └── Surface.py
├── Block
│   ├── BaseBlock.py
│   ├── BlockingBlcok.py
│   ├── BoxBlock.py
│   ├── CornerBlock.py
│   ├── DoorBlock.py
│   ├── GroundBlock.py
│   ├── __init__.py
│   ├── NextBlock.py
│   └── WallBlock.py
├── Coin
│   ├── BaseCoin.py
│   ├── EnergyCoin.py
│   ├── __init__.py
│   ├── MoneyCoin.py
├── Compute
│   ├── BlockCompute.py
│   ├── DistanceCompute.py
│   ├── __init__.py
│   ├── MoveCompute.py
│   ├── PositionCompute.py
│   └── SpaceCompute.py
├── Creator
│   ├── BadActorCreator.py
│   ├── __init__.py
│   ├── MapCreator.py
├── Data
│   ├── ActorData.py
│   ├── AllData.py
│   ├── BlockData.py
│   ├── EventData.py
│   ├── GameData.py
│   ├── InfoBarData.py
│   ├── __init__.py
│   ├── ShareData.py
│   ├── SpaceData.py
│   └── SpecialData.py
├── docs
│   ├── ...
├── Egg
│   ├── BaseEgg.py
│   ├── GunEgg.py
│   ├── HandGunEgg.py
│   ├── __init__.py
│   ├── NoneEgg.py
├── Game.py
├── Group
│   ├── BadActorGroup.py
│   ├── CoinGroup.py
│   ├── DropThingGroup.py
│   ├── HireActorGroup.py
│   ├── __init__.py
│   ├── MapGroup.py
│   ├── SellActorGroup.py
│   └── TreasureGroup.py
├── GUI
│   ├── Button.py
│   ├── __init__.py
│   ├── Label.py
│   ├── Manager.py
├── InfoBar
│   ├── BaseInfoBar.py
│   ├── BloodInfoBar.py
│   ├── DropThingInfoBar.py
│   ├── EnergyInfoBar.py
│   ├── __init__.py
│   ├── MoneyInfoBar.py
│   ├── ProtectionInfoBar.py
│   ├── SkillInfoBar.py
│   └── ThingInfoBar.py
├── __init__.py
├── Logo
│   ├── __init__.py
│   ├── logo.py
│   └── README.md
├── MapLoader
│   ├── BadActorLoader.py
│   ├── __init__.py
│   ├── MapLoader.py
│   └── SpaceLoader.py
├── Math
│   ├── __init__.py
│   ├── Math.py
├── requirements.txt
├── Res
│   ├── GUI_Theme
│   │   ├── data
│   │   │   ├── fonts
│   │   │   │   ├── __init__.py
│   │   │   │   ├── VonwaonBitmap-12px.ttf
│   │   │   │   └── VonwaonBitmap-16px.ttf
│   │   │   ├── __init__.py
│   │   ├── Infobar
│   │   │   ├── __init__.py
│   │   │   ├── money_info_bar.json
│   │   │   └── thing_info_bar.json
│   │   ├── __init__.py
│   │   ├── Screen
│   │   │   ├── info_screen.json
│   │   │   ├── __init__.py
│   │   │   └── title_screen.json
│   │   └── Speak
│   │       ├── base_speak.json
│   │       └── __init__.py
│   ├── __init__.py
│   ├── Map
│   │   ├── ...
│   ├── MapModel
│   │   ├── ...
│   ├── Picture
│   │   ├── ...
├── Screen
│   ├── EndSceen.py
│   ├── __init__.py
│   ├── PauseSceen.py
│   ├── StartSceen.py
│   ├── SystemInfoScreen.py
│   └── WinSceen.py
├── Space
│   ├── BaseSpace.py
│   ├── HeightCrossSpace.py
│   ├── __init__.py
│   ├── RoomSpace
│   │   ├── BadActorRoomSpace.py
│   │   ├── BaseRoomSpace.py
│   │   ├── copy.py
│   │   ├── __init__.py
│   │   ├── SellActorRoomSpace.py
│   │   └── TreasureRoomSpace.py
│   ├── WidthCrossSpace.py
│   └── WorldSpace.py
├── Speak
│   ├── BaseSpeak.py
│   ├── __init__.py
├── Test
│   ├── __init__.py
│   └── test.py
├── Thing
│   ├── BaseThing.py
│   ├── BloodDrinkThing.py
│   ├── EnergyDrinkThing.py
│   ├── GunThing.py
│   ├── HandGunThing.py
│   ├── __init__.py
│   └── ThingList.py
└── Treasure
    ├── BaseTreasure.py
    ├── EnergyTreasure.py
    ├── __init__.py
```

## 项目文件夹对应功能

| 文件夹名称 | 功能实现 |
|----------|---------|
|Actor|游戏中可交互角色|
|BetterPygame|自定义函数，弥补Pygame的不足|
|Block|构成地图的方块|
|Coin|掉落的能量以及金币|
|Compute|提供一系列常用计算函数|
|Creator|基于地图模板的随即生成器|
|Data|项目中全局共享的动/静态数据|
|doc|老文档，未来版本淘汰|
|docs|新文档，基于Docsify，也就是您现在浏览的页面|
|Egg|枪械射击的子弹|
|Group|组，用于批量处理|
|GUI|游戏中的按钮等UI界面|
|InfoBar|人物的血条等|
|Logo|程序开始的Logo画面|
|MapLoader|地图加载器|
|Math|提供关于数学的函数|
|Res|资源文件，包括图片文件，地图文件和GUI配置文件等|
|Screen|游戏开始，暂停等屏幕|
|Space|游戏地图空间|
|Speak|游戏中Actor的对话交互，支持中文|
|Test|测试代码|
|Thing|游戏中的枪械|
|Treasure|宝箱，下版本将从Actor继承以重写|
