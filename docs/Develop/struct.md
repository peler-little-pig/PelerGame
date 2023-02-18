# 项目结构

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