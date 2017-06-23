# -*- coding: utf-8 -*-

import pytest
from gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert Item("foo", -1, 0) == gilded_rose.items[0]


def test_each_day_both_lower_down():
    items = [Item("foo", 3, 5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert Item("foo", 2, 4) == gilded_rose.items[0]


def test_once_date_passed_quality_degrades_twice_as_fast():
    items = [Item("foo", 0, 5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert Item("foo", -1, 3) == gilded_rose.items[0]

    gilded_rose.update_quality()
    
    assert Item("foo", -2, 1) == gilded_rose.items[0]


def test_quality_never_negative():
    items = [Item("foo", 3, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert Item("foo", 2, 0) == gilded_rose.items[0]

    items = [Item("foo", -1, 1)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert Item("foo", -2, 0) == gilded_rose.items[0]


def test_aged_brie_increases_quality():
    items = [Item("Aged Brie", 3, 5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert Item("Aged Brie", 2, 6) == gilded_rose.items[0]


def test_quality_never_more_than_50():
    items = [Item("Aged Brie", 3, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert Item("Aged Brie", 2, 50) == gilded_rose.items[0]


def test_sulfuras_never_sold_and_never_decreases_quality():
    items = [Item("Sulfuras, Hand of Ragnaros", 3, 7)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert Item("Sulfuras, Hand of Ragnaros", 3, 7) == gilded_rose.items[0]


@pytest.mark.parametrize("sell_in,quality,expected_quality", [
    (13, 5, 6),
    (11, 5, 6),
    (10, 5, 7),
    (6, 5, 7),
    (5, 5, 8),
    (1, 5, 8),
    (0, 5, 0),
    (-3, 5, 0),
])
def test_backstage_passes_increases_quality_with_some_rules(sell_in, quality, expected_quality):
    items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert Item("Backstage passes to a TAFKAL80ETC concert", sell_in - 1, expected_quality) == gilded_rose.items[0]


@pytest.mark.skip
def test_conjuras_degrades_quality_twice_as_fast():
    items = [Item("Conjuras", 1, 8)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert Item("Conjuras", 0, 6) == gilded_rose.items[0]

    gilded_rose.update_quality()
    
    assert Item("Conjuras", -1, 2) == gilded_rose.items[0]
