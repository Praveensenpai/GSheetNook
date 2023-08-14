import gspread
import pandas as pd


class GoogleSheet:
    is_spread_worksheet_set = False

    def __init__(
        self,
        service_account_file: str = "service_account.json",
        spreadsheet: str = None,
    ) -> None:
        self.sa = gspread.service_account(service_account_file)
        self.sh = None

        if spreadsheet:
            self.set_spread_worksheet(spreadsheet)

    def set_spread_worksheet(self, spreadsheet: str) -> None:
        self.sh = self.sa.open(spreadsheet)
        self.is_spread_worksheet_set = True

    def get_sheet(self, sheet: str) -> pd.DataFrame:
        if not self.is_spread_worksheet_set:
            raise ValueError(
                "Spreadsheet worksheet has not been set. Call set_spread_worksheet first."
            )
        wks = self.sh.worksheet(sheet)
        data = wks.get_all_values()
        return pd.DataFrame(data[1:], columns=data[0])
