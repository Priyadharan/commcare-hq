from __future__ import absolute_import
from __future__ import unicode_literals

from dateutil.relativedelta import relativedelta
from custom.icds_reports.const import AGG_DAILY_FEEDING_TABLE
from custom.icds_reports.utils.aggregation_helpers import BaseICDSAggregationHelper, month_formatter


class DailyFeedingFormsChildHealthAggregationHelper(BaseICDSAggregationHelper):
    ucr_data_source_id = 'dashboard_child_health_daily_feeding_forms'
    tablename = AGG_DAILY_FEEDING_TABLE

    def drop_table_query(self):
        return (
            'DELETE FROM "{}" WHERE month=%(month)s AND state_id = %(state)s'.format(self.tablename),
            {'month': month_formatter(self.month), 'state': self.state_id}
        )

    def aggregation_query(self):
        current_month_start = month_formatter(self.month)
        next_month_start = month_formatter(self.month + relativedelta(months=1))

        query_params = {
            "month": month_formatter(self.month),
            "state_id": self.state_id,
            "current_month_start": current_month_start,
            "next_month_start": next_month_start,
        }

        return """
        INSERT INTO "{tablename}" (
          state_id, supervisor_id, month, case_id, latest_time_end_processed,
          sum_attended_child_ids, lunch_count
        ) (
          SELECT DISTINCT ON (child_health_case_id)
            %(state_id)s AS state_id,
            supervisor_id,
            %(month)s AS month,
            child_health_case_id AS case_id,
            MAX(timeend) OVER w AS latest_time_end_processed,
            SUM(attended_child_ids) OVER w AS sum_attended_child_ids,
            SUM(lunch) OVER w AS lunch_count
          FROM "{ucr_tablename}"
          WHERE state_id = %(state_id)s AND
                timeend >= %(current_month_start)s AND timeend < %(next_month_start)s AND
                child_health_case_id IS NOT NULL
          WINDOW w AS (PARTITION BY supervisor_id, child_health_case_id)
        )
        """.format(
            ucr_tablename=self.ucr_tablename,
            tablename=self.tablename
        ), query_params
