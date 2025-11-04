from enums.report_enum import ReportEnum
from report.report_config import ReportConfig

class Report:
    def __init__(self, data: list[dict]):
        self.data = data
        self.NAME_WIDTH = ReportConfig.NAME_WIDTH
        self.EMAIL_WIDTH = ReportConfig.EMAIL_WIDTH
        self.COURSE_WIDTH = ReportConfig.COURSE_WIDTH
        self.AGE_WIDTH = ReportConfig.AGE_WIDTH
        self.TOTAL_WIDTH = self.NAME_WIDTH + self.EMAIL_WIDTH + self.COURSE_WIDTH + self.AGE_WIDTH

    def display(self):
        print(ReportEnum.SUBSCRIBERS_QUERY.value)  # Título da consulta
        print(f"\n{ReportEnum.SUBSCRIPTIONS_TABLE_DATA.value}")  # Subtítulo
        print("-" * self.TOTAL_WIDTH)

        header = f"{'Name':<{self.NAME_WIDTH}}{'Email':<{self.EMAIL_WIDTH}}{'Course':<{self.COURSE_WIDTH}}{'Age':>{self.AGE_WIDTH}}"
        print(header)
        print("-" * self.TOTAL_WIDTH)

        for row in self.data:
            name = row['name']
            email = row['email']
            course = row['course']
            age = str(row['age']).zfill(self.AGE_WIDTH)

            line_output = f"{name:<{self.NAME_WIDTH}}{email:<{self.EMAIL_WIDTH}}{course:<{self.COURSE_WIDTH}}{age:>{self.AGE_WIDTH}}"
            print(line_output)
        print('=' * self.TOTAL_WIDTH)
        registers_found = len(self.data)
        print(f"{registers_found} registers found")
