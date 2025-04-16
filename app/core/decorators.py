from functools import wraps
# from ..services.schedule_service import sort_schedules_by_season


# def sort_sch(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(**args, **kwargs)
#         if result is not None:
#             return sort_schedules_by_season(result)
#         return result

#     return wrapper
