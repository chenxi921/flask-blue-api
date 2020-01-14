# -*- coding: utf-8 -*-
import logging, time

file_name = '%s.log' % (time.strftime("%Y-%m-%d"))

logging.basicConfig(
    level=logging.DEBUG,
    filename='logs/%s' % file_name,
    format="[%(asctime)s]-[%(levelname)s]: %(message)s",
)

logger = logging.getLogger("api")

