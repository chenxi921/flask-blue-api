# -*- coding: utf-8 -*-
"""
    Created by Space on 2019/12/19 18:47
"""
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]-[%(levelname)s]: %(message)s",
)

logger = logging.getLogger("api.v1")
