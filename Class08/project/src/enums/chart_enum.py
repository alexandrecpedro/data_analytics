from enum import Enum

class BarChartEnum(Enum):
    REVENUE_UNITS_SUBHEADER = 'Total Revenue per Unit'
    REVENUE_UNITS_TITLE = '💰 Total Revenue per Unit'
    REVENUE_UNITS_XAXIS_LABEL = 'Unit'
    REVENUE_UNITS_YAXIS_LABEL = 'Revenue (R$)'

    UNIT_APPOINTMENTS_SUBHEADER = 'Number of Appointments per Unit'
    UNIT_APPOINTMENTS_TITLE = 'Appointments per Unit'
    UNIT_APPOINTMENTS_XAXIS_LABEL = 'Unit'
    UNIT_APPOINTMENTS_YAXIS_LABEL = 'Total Appointments'


class DonutChartEnum(Enum):
    APPOINTMENTS_TYPE_FORMAT_VALUES = '.1%'
    APPOINTMENTS_TYPE_LEGEND_TITLE = 'Specialty'
    APPOINTMENTS_TYPE_SUBHEADER = 'Number of Appointments per Specialty'
    APPOINTMENTS_TYPE_TITLE = 'Appointments per Specialty'
    APPOINTMENTS_TYPE_TOOLTIP_TITLE = 'Appointment Type'

    MARK_ARC_INNER_RADIUS = 40
    MARK_ARC_OUTER_RADIUS = 120
    MARK_TEXT_COLOR = 'white'
    MARK_TEXT_RADIUS = 145
    PERCENTAGE = 'percentage'