from nose.tools import eq_
from gothonweb.planisphere import *


def test_room_generic_death():
    room = load_room('generic_death')
    paths = {}

    eq_(room.name, "Death")
    eq_(room.paths, paths)


def test_room_central_corridor():
    room = load_room('central_corridor')
    paths = {
        'shoot!': generic_death,
        'dodge!': generic_death,
        'tell a joke': laser_weapon_armory
    }

    eq_(room.name, "Central Corridor")
    eq_(room.paths, paths)


def test_room_laser_weapon_armory():
    room = load_room('laser_weapon_armory')
    paths = {
        '0132': the_bridge,
        '*': generic_death
    }

    eq_(room.name, "Laser Weapon Armory")
    eq_(room.paths, paths)


def test_room_the_bridge():
    room = load_room('the_bridge')
    paths = {
        'throw the bomb': generic_death,
        'slowly place the bomb': escape_pod
    }

    eq_(room.name, "The Bridge")
    eq_(room.paths, paths)


def test_room_escape_pod():
    room = load_room('escape_pod')
    paths = {
        '2': the_end_winner,
        '*': the_end_loser
    }

    eq_(room.name, "Escape Pod")
    eq_(room.paths, paths)


def test_room_the_end_winner():
    room = load_room('the_end_winner')
    paths = {}

    eq_(room.name, "The End")
    eq_(room.paths, paths)


def test_room_the_end_loser():
    room = load_room('the_end_loser')
    paths = {}

    eq_(room.name, "The End")
    eq_(room.paths, paths)


# def test_room_paths():
#     center = Room("Center", "Test room in the center.")
#     north = Room("North", "Test room in the north.")
#     south = Room("South", "Test room in the south.")

#     center.add_paths({'north': north, 'south': south})
#     assert_equal(center.go('north'), north)
#     assert_equal(center.go('south'), south)

# def test_map():
#     start = Room("Start", "You can go west and down a hole.")
#     west = Room("Trees", "There are trees here, you can go east.")
#     down = Room("Dungeon", "It's dark down here, you can go up.")

#     start.add_paths({'west': west, 'down': down})
#     west.add_paths({'east': start})
#     down.add_paths({'up': start})

#     assert_equal(start.go('west'), west)
#     assert_equal(start.go('west').go('east'), start)
#     assert_equal(start.go('down').go('up'), start)

def test_map():
    start_room = load_room(START)
    eq_(start_room.go('shoot!'), generic_death)
    eq_(start_room.go('dodge!'), generic_death)
    eq_(start_room.go('tell a joke'), laser_weapon_armory)

