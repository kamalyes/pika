from typing import List

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.core.handler.executor import Executor
from app.core.handler.jsonres import PikaResponse
from app.enums.SysVarEnum import PikaGlobalVarEnum


class Scheduler(object):
    scheduler: AsyncIOScheduler = None

    @staticmethod
    def init(scheduler):
        Scheduler.scheduler = scheduler

    @staticmethod
    def configure(**kwargs):
        Scheduler.scheduler.configure(**kwargs)

    @staticmethod
    def start():
        Scheduler.scheduler.start()

    @staticmethod
    def add_test_plan(plan_id, plan_name, cron):
        return Scheduler.scheduler.add_job(func=Executor.run_test_plan, args=(plan_id,),
                                           name=plan_name, id=str(plan_id),
                                           trigger=CronTrigger.from_crontab(cron))

    @staticmethod
    def edit_test_plan(plan_id, plan_name, cron):
        """
        通过测试计划id,更新测试计划任务的cron,name等数据
        Args:
            plan_id:
            plan_name:
            cron:

        Returns:

        """
        job = Scheduler.scheduler.get_job(str(plan_id))
        if job is None:
            # 新增job
            return Scheduler.add_test_plan(plan_id, plan_name, cron)
        Scheduler.scheduler.modify_job(job_id=str(plan_id), trigger=CronTrigger.from_crontab(cron),
                                       name=plan_name)
        Scheduler.scheduler.pause_job(str(plan_id))
        Scheduler.scheduler.resume_job(str(plan_id))

    @staticmethod
    def pause_resume_test_plan(plan_id, status):
        """
        暂停或恢复测试计划,会影响到next_run_at
        Args:
            plan_id:
            status:

        Returns:

        """
        if status:
            Scheduler.scheduler.resume_job(job_id=str(plan_id))
        else:
            Scheduler.scheduler.pause_job(job_id=str(plan_id))

    @staticmethod
    def remove(plan_id):
        """
        删除job,当删除测试计划时,调用此方法
        Args:
            plan_id:

        Returns:

        """
        Scheduler.scheduler.remove_job(str(plan_id))

    @staticmethod
    def list_test_plan(data: List):
        ans = []
        for d, follow in data:
            temp = PikaResponse.model_to_dict(d)
            temp['follow'] = follow is not None
            job = Scheduler.scheduler.get_job(str(temp.get('id')))
            if job is None:
                # 说明job初始化失败了
                temp["state"] = 2
                ans.append(temp)
                continue
            if job.next_run_time is None:
                # 说明job被暂停了
                temp["state"] = 3
            else:
                temp["next_run"] = job.next_run_time.strftime(
                    PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS)
            ans.append(temp)
        return ans
