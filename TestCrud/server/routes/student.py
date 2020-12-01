# -*- coding: utf-8 -*-
"""
@author: anuja
"""
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from TestCrud\server\database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from TestCrud\server\models\student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()