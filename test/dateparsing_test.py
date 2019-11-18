from datetime import datetime

import utils


def test_date_parsing():
	base_time = utils.datetime_force_utc(datetime.strptime("2019-01-01 01:23:45", "%Y-%m-%d %H:%M:%S"))

	pairs = [
		["1 day", "2019-01-02 01:23:45"],
		["365 days", "2020-01-01 01:23:45"],
		["2 weeks", "2019-01-15 01:23:45"],
		["3 years", "2022-01-01 01:23:45"],
		["3 months", "2019-04-01 01:23:45"],
		["24 hours", "2019-01-02 01:23:45"],
		["5 hrs", "2019-01-01 06:23:45"],
		["20 minutes", "2019-01-01 01:43:45"],
		["5 seconds", "2019-01-01 01:23:50"],
		["tomorrow", "2019-01-02 01:23:45"],
		["Next Thursday at 4pm", "2019-01-10 16:00:00"],
		["Tonight", "2019-01-01 21:00:00"],
		["2 Hours After Noon", "2019-01-01 14:00:00"],
		["eoy", "2019-12-31 09:00:00"],
		["eom", "2019-01-31 09:00:00"],
		["eod", "2019-01-01 17:00:00"],
		["2022-01-01", "2022-01-01 00:00:00"],
		["10/15/19", "2019-10-15 00:00:00"],
		["April 9, 2020", "2020-04-09 00:00:00"],
		["January 13th, 2020", "2020-01-13 00:00:00"],
		["January 5th 2020", "2020-01-05 00:00:00"],
		["June 2nd", "2019-06-02 00:00:00"],
		["November 2", "2019-11-02 00:00:00"],
		["August 25, 2018, at 4pm", "2018-08-25 16:00:00"],
		["September 1, 2019 14:00:00", "2019-09-01 14:00:00"],
		["august", "2019-08-01 00:00:00"],
		["September", "2019-09-01 00:00:00"],
		["2025", "2025-01-01 00:00:00"],
		["2pm", "2019-01-01 14:00:00"],
		["7:20 pm", "2019-01-01 19:20:00"],
		["72hr", "2019-01-04 01:23:45"],
		["1d", "2019-01-02 01:23:45"],
		["1yr", "2020-01-01 01:23:45"],
		["7h", "2019-01-01 08:23:45"],
		["35m", "2019-01-01 01:58:45"],
	]

	for time_string, expected_string in pairs:
		result_date = utils.parse_time(time_string, base_time, "UTC")
		expected_date = utils.datetime_force_utc(datetime.strptime(expected_string, "%Y-%m-%d %H:%M:%S"))
		assert result_date == expected_date, f"`{time_string}` as `{result_date}` != `{expected_date}`"


def test_date_parsing_timezone():
	base_time = utils.datetime_force_utc(datetime.strptime("2019-01-01 01:23:45", "%Y-%m-%d %H:%M:%S"))

	timezones = [
		"America/Los_Angeles",
		"America/Denver",
		"America/Chicago",
		"America/New_York",
		"Australia/Sydney",
		"Europe/Brussels",
	]
	pairs = [
		["1 day", 						["2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45"]],
		["365 days", 					["2020-01-01 01:23:45", "2020-01-01 01:23:45", "2020-01-01 01:23:45", "2020-01-01 01:23:45", "2020-01-01 01:23:45", "2020-01-01 01:23:45"]],
		["2 weeks", 					["2019-01-15 01:23:45", "2019-01-15 01:23:45", "2019-01-15 01:23:45", "2019-01-15 01:23:45", "2019-01-15 01:23:45", "2019-01-15 01:23:45"]],
		["3 years", 					["2022-01-01 01:23:45", "2022-01-01 01:23:45", "2022-01-01 01:23:45", "2022-01-01 01:23:45", "2022-01-01 01:23:45", "2022-01-01 01:23:45"]],
		["3 months", 					["2019-04-01 00:23:45", "2019-04-01 00:23:45", "2019-04-01 00:23:45", "2019-04-01 00:23:45", "2019-04-01 01:23:45", "2019-04-01 00:23:45"]],
		["24 hours", 					["2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45"]],
		["5 hrs", 						["2019-01-01 06:23:45", "2019-01-01 06:23:45", "2019-01-01 06:23:45", "2019-01-01 06:23:45", "2019-01-01 06:23:45", "2019-01-01 06:23:45"]],
		["20 minutes", 					["2019-01-01 01:43:45", "2019-01-01 01:43:45", "2019-01-01 01:43:45", "2019-01-01 01:43:45", "2019-01-01 01:43:45", "2019-01-01 01:43:45"]],
		["5 seconds", 					["2019-01-01 01:23:50", "2019-01-01 01:23:50", "2019-01-01 01:23:50", "2019-01-01 01:23:50", "2019-01-01 01:23:50", "2019-01-01 01:23:50"]],
		["tomorrow", 					["2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45"]],
		["Next Thursday at 4pm", 		["2019-01-11 00:00:00", "2019-01-10 23:00:00", "2019-01-10 22:00:00", "2019-01-10 21:00:00", "2019-01-10 05:00:00", "2019-01-10 15:00:00"]],
		["Tonight", 					["2019-01-01 05:00:00", "2019-01-01 04:00:00", "2019-01-01 03:00:00", "2019-01-01 02:00:00", "2019-01-01 10:00:00", "2019-01-01 20:00:00"]],
		["2 Hours After Noon", 			["2018-12-31 22:00:00", "2018-12-31 21:00:00", "2018-12-31 20:00:00", "2018-12-31 19:00:00", "2019-01-01 03:00:00", "2019-01-01 13:00:00"]],
		["eoy", 						["2018-12-31 17:00:00", "2018-12-31 16:00:00", "2018-12-31 15:00:00", "2018-12-31 14:00:00", "2019-12-30 22:00:00", "2019-12-31 08:00:00"]],
		["eom", 						["2018-12-31 17:00:00", "2018-12-31 16:00:00", "2018-12-31 15:00:00", "2018-12-31 14:00:00", "2019-01-30 22:00:00", "2019-01-31 08:00:00"]],
		["eod", 						["2019-01-01 01:00:00", "2019-01-01 00:00:00", "2018-12-31 23:00:00", "2018-12-31 22:00:00", "2019-01-01 06:00:00", "2019-01-01 16:00:00"]],
		["2022-01-01", 					["2022-01-01 08:00:00", "2022-01-01 07:00:00", "2022-01-01 06:00:00", "2022-01-01 05:00:00", "2021-12-31 13:00:00", "2021-12-31 23:00:00"]],
		["10/15/19", 					["2019-10-15 07:00:00", "2019-10-15 06:00:00", "2019-10-15 05:00:00", "2019-10-15 04:00:00", "2019-10-14 13:00:00", "2019-10-14 22:00:00"]],
		["April 9, 2020", 				["2020-04-09 07:00:00", "2020-04-09 06:00:00", "2020-04-09 05:00:00", "2020-04-09 04:00:00", "2020-04-08 14:00:00", "2020-04-08 22:00:00"]],
		["January 13th, 2020", 			["2020-01-13 08:00:00", "2020-01-13 07:00:00", "2020-01-13 06:00:00", "2020-01-13 05:00:00", "2020-01-12 13:00:00", "2020-01-12 23:00:00"]],
		["January 5th 2020", 			["2020-01-05 08:00:00", "2020-01-05 07:00:00", "2020-01-05 06:00:00", "2020-01-05 05:00:00", "2020-01-04 13:00:00", "2020-01-04 23:00:00"]],
		["June 2nd", 					["2019-06-02 07:00:00", "2019-06-02 06:00:00", "2019-06-02 05:00:00", "2019-06-02 04:00:00", "2019-06-01 14:00:00", "2019-06-01 22:00:00"]],
		["November 2", 					["2019-11-02 07:00:00", "2019-11-02 06:00:00", "2019-11-02 05:00:00", "2019-11-02 04:00:00", "2019-11-01 13:00:00", "2019-11-01 23:00:00"]],
		["August 25, 2018, at 4pm", 	["2018-08-25 23:00:00", "2018-08-25 22:00:00", "2018-08-25 21:00:00", "2018-08-25 20:00:00", "2018-08-25 06:00:00", "2018-08-25 14:00:00"]],
		["September 1, 2019 14:00:00", 	["2019-09-01 21:00:00", "2019-09-01 20:00:00", "2019-09-01 19:00:00", "2019-09-01 18:00:00", "2019-09-01 04:00:00", "2019-09-01 12:00:00"]],
		["august", 						["2019-08-31 07:00:00", "2019-08-31 06:00:00", "2019-08-31 05:00:00", "2019-08-31 04:00:00", "2019-07-31 14:00:00", "2019-07-31 22:00:00"]],
		["September", 					["2019-09-30 07:00:00", "2019-09-30 06:00:00", "2019-09-30 05:00:00", "2019-09-30 04:00:00", "2019-08-31 14:00:00", "2019-08-31 22:00:00"]],
		["2025", 						["2025-12-31 08:00:00", "2025-12-31 07:00:00", "2025-12-31 06:00:00", "2025-12-31 05:00:00", "2024-12-31 13:00:00", "2024-12-31 23:00:00"]],
		["2pm", 						["2019-01-01 22:00:00", "2019-01-01 21:00:00", "2019-01-01 20:00:00", "2019-01-01 19:00:00", "2019-01-01 03:00:00", "2019-01-01 13:00:00"]],
		["7:20 pm", 					["2019-01-01 03:20:00", "2019-01-01 02:20:00", "2019-01-02 01:20:00", "2019-01-02 00:20:00", "2019-01-01 08:20:00", "2019-01-01 18:20:00"]],
		["72hr", 						["2019-01-04 01:23:45", "2019-01-04 01:23:45", "2019-01-04 01:23:45", "2019-01-04 01:23:45", "2019-01-04 01:23:45", "2019-01-04 01:23:45"]],
		["1d", 							["2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45", "2019-01-02 01:23:45"]],
		["1yr", 						["2020-01-01 01:23:45", "2020-01-01 01:23:45", "2020-01-01 01:23:45", "2020-01-01 01:23:45", "2020-01-01 01:23:45", "2020-01-01 01:23:45"]],
		["7h", 							["2019-01-01 08:23:45", "2019-01-01 08:23:45", "2019-01-01 08:23:45", "2019-01-01 08:23:45", "2019-01-01 08:23:45", "2019-01-01 08:23:45"]],
		["35m", 						["2019-01-01 01:58:45", "2019-01-01 01:58:45", "2019-01-01 01:58:45", "2019-01-01 01:58:45", "2019-01-01 01:58:45", "2019-01-01 01:58:45"]],
	]

	for time_string, expected_strings in pairs:
		for i, timezone in enumerate(timezones):
			result_date = utils.parse_time(time_string, base_time, timezone)
			expected_date = utils.datetime_force_utc(datetime.strptime(expected_strings[i], "%Y-%m-%d %H:%M:%S"))
			assert result_date == expected_date, f"`{time_string}`, `{timezone}` as `{result_date}` != `{expected_date}`"