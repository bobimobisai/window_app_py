import flet
from flet import Page, Text, ElevatedButton, Column


class MyApp:
    def __init__(self):
        self.title = "My Multi-Page App"
        self.theme_mode = "light"
        self.vertical_alignment = flet.MainAxisAlignment.CENTER

    def main(self, page: Page):
        page.title = self.title
        page.theme_mode = self.theme_mode
        page.vertical_alignment = self.vertical_alignment
        page.clean()
        page.add(
            flet.Row(
                [
                    ElevatedButton(
                        text="Go to Page 1", on_click=lambda e: self.show_page_1(page)
                    ),
                    ElevatedButton(
                        text="Go to Page 2", on_click=lambda e: self.show_page_2(page)
                    ),
                ],
                alignment=self.vertical_alignment,
            )
        )

    def show_page_1(self, page: Page):
        page.clean()
        page.add(
            flet.Row(
                [
                    Text("This is Page 1"),
                    ElevatedButton(
                        text="Back to Home", on_click=lambda e: self.main(page)
                    ),
                ],
                alignment=self.vertical_alignment,
            )
        )

    def show_page_2(self, page: Page):
        page.clean()
        page.add(
            flet.Row(
                [
                    Text("This is Page 2"),
                    ElevatedButton(
                        text="Back to Home", on_click=lambda e: self.main(page)
                    ),
                ],
                alignment=self.vertical_alignment,
            )
        )

    def __call__(self, page: Page):
        self.main(page)
