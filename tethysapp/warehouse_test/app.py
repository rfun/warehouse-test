from tethys_sdk.base import TethysAppBase, url_map_maker


class WarehouseTest(TethysAppBase):
    """
    Tethys app class for Warehouse Test.
    """

    name = 'Warehouse Test'
    index = 'warehouse_test:home'
    icon = 'warehouse_test/images/icon.gif'
    package = 'warehouse_test'
    root_url = 'warehouse-test'
    color = '#f39c12'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='warehouse-test',
                controller='warehouse_test.controllers.home'
            ),
        )

        return url_maps
