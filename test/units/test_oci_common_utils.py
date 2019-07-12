# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from ansible.module_utils.oracle import oci_common_utils


def test_is_dict_subset_when_source_or_target_are_None():
    assert oci_common_utils.is_dict_subset(None, None) is False
    assert oci_common_utils.is_dict_subset({}, None) is False
    assert oci_common_utils.is_dict_subset(None, {}) is False


def test_is_dict_subset_when_source_or_target_are_not_dicts():
    assert oci_common_utils.is_dict_subset([], {}) is False
    assert oci_common_utils.is_dict_subset([], []) is False
    assert oci_common_utils.is_dict_subset("testsourcestr", {}) is False
    assert oci_common_utils.is_dict_subset(1, {}) is False
    assert oci_common_utils.is_dict_subset(True, {}) is False
    assert oci_common_utils.is_dict_subset({}, "testtargetstr") is False
    assert oci_common_utils.is_dict_subset({}, 1) is False
    assert oci_common_utils.is_dict_subset({}, True) is False


def test_is_dict_subset_when_source_and_target_are_empty():
    assert oci_common_utils.is_dict_subset({}, {}) is True


def test_is_dict_subset_when_source_has_more_keys():
    s = {"key1": "val1"}
    t = {}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": "val2"}
    t = {"key1": "val1"}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1"}}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey3": "subval3"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    assert oci_common_utils.is_dict_subset(s, t) is True


def test_is_dict_subset_when_source_has_less_keys():
    s = {"key1": "val1"}
    t = {"key1": "val1", "key2": "val2"}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1"}
    t = {"key1": "val1", "key2": "val2", "key3": "val3"}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {}
    t = {"key1": "val1", "key2": "val2"}
    assert oci_common_utils.is_dict_subset(s, t) is True


def test_is_dict_subset_when_dicts_have_list_values():
    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item2", "item3"]}
    assert oci_common_utils.is_dict_subset(s, t) is False

    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item2", "item3", "item1"]}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item1", "item2", "item3", "item4"]}
    assert oci_common_utils.is_dict_subset(s, t) is False


def test_is_dict_subset_when_dicts_have_dict_values():
    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}}
    t = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": "subval2"}, "subkey3": {"subkey4": "subval4"}},
    }
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": {"subkey3": "subval3"}}}}
    t = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": {"subkey3": "subval3", "subkey4": "subval4"}}},
    }
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}, "key3": {}}
    t = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": "subval2"}, "subkey3": {"subkey4": "subval4"}},
    }
    assert oci_common_utils.is_dict_subset(s, t) is True


def test_is_dict_subset_returns_False_when_dicts_are_different():

    s = {"key1": "val1", "key2": "val2"}
    t = {"key1": "val1", "key2": "differentval2"}
    assert oci_common_utils.is_dict_subset(s, t) is False

    s = {"key1": "val1", "key2": "val2", "key3": {"subkey1": "subval1"}}
    t = {"key1": "val1", "key2": "val2", "key3": {"subkey1": "differentval1"}}
    assert oci_common_utils.is_dict_subset(s, t) is False

    s = {"key1": "val1", "key2": "val2", "key3": {"subkey1": True}}
    t = {"key1": "val1", "key2": "val2", "key3": {"subkey1": False}}
    assert oci_common_utils.is_dict_subset(s, t) is False

    s = {"key1": "val1", "key2": "val2", "key3": {"subkey1": 1}}
    t = {"key1": "val1", "key2": "val2", "key3": {"subkey1": "subval1"}}
    assert oci_common_utils.is_dict_subset(s, t) is False


def test_are_dicts_equal_when_source_or_target_are_None():
    assert oci_common_utils.are_dicts_equal(None, None) is False
    assert oci_common_utils.are_dicts_equal({}, None) is False
    assert oci_common_utils.are_dicts_equal(None, {}) is False


def test_are_dicts_equal_when_source_or_target_are_not_dicts():
    assert oci_common_utils.are_dicts_equal([], {}) is False
    assert oci_common_utils.are_dicts_equal([], []) is False
    assert oci_common_utils.are_dicts_equal("testsourcestr", {}) is False
    assert oci_common_utils.are_dicts_equal(1, {}) is False
    assert oci_common_utils.are_dicts_equal(True, {}) is False
    assert oci_common_utils.are_dicts_equal({}, "testtargetstr") is False
    assert oci_common_utils.are_dicts_equal({}, 1) is False
    assert oci_common_utils.are_dicts_equal({}, True) is False


def test_are_dicts_equal_when_source_and_target_are_empty():
    assert oci_common_utils.are_dicts_equal({}, {}) is True


def test_are_dicts_equal_when_source_has_more_keys():
    s = {"key1": "val1"}
    t = {}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {"key1": "val1", "key2": "val2"}
    t = {"key1": "val1"}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1"}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {
        "key1": "val1",
        "key2": {"subkey1": "subval1", "subkey3": "subval3"},
        "key3": "val3",
    }
    t = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_source_has_less_keys():
    s = {"key1": "val1"}
    t = {"key1": "val1", "key2": "val2"}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {"key1": "val1"}
    t = {"key1": "val1", "key2": "val2", "key3": "val3"}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {}
    t = {"key1": "val1", "key2": "val2"}
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_source_subdicts_have_less_keys():
    s = {"key1": {"subkey1": "subval1"}}
    t = {"key1": {"subkey1": "subval1", "subkey2": "subval2"}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": {"subkey1": {"subkey2": "subval2"}}}
    t = {"key1": {"subkey1": {"subkey2": "subval2", "subkey3": "subval3"}}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": {"subkey1": {}}}
    t = {"key1": {"subkey1": {"subkey2": "subval2", "subkey3": "subval3"}}}
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_source_subdicts_have_more_keys():
    s = {"key1": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": {"subkey1": "subval1"}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": {"subkey1": {"subkey2": "subval2", "subkey3": "subval3"}}}
    t = {"key1": {"subkey1": {"subkey2": "subval2"}}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": {"subkey1": {"subkey2": "subval2", "subkey3": "subval3"}}}
    t = {"key1": {"subkey1": {}}}
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_dicts_have_list_values():
    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item2", "item3"]}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item2", "item3", "item1"]}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item1", "item2", "item3", "item4"]}
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_dicts_have_dict_values():
    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}}
    t = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": "subval2"}, "subkey3": {"subkey4": "subval4"}},
    }
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}, "key3": {}}
    t = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": "subval2"}, "subkey3": {"subkey4": "subval4"}},
    }
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_dicts_have_different_values():
    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "differentsubval2"}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}}
    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "differentsubval2"}}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}, "key3": {}}
    s = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": "differentsubval2"}},
        "key3": {},
    }
    assert oci_common_utils.are_dicts_equal(s, t) is False
