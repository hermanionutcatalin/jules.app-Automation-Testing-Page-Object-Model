import unittest
import HtmlTestRunner

from final_project.test import test_pagina_home
from final_project.test import test_pagina_sign


class SuiteHomeSign(unittest.TestCase):

    smoke_test = unittest.TestSuite()
    smoke_test.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(test_pagina_home.TestPaginaHome),
        unittest.defaultTestLoader.loadTestsFromTestCase(test_pagina_sign.TestPaginaSign),

    ])
    runner = HtmlTestRunner.HTMLTestRunner(
        combine_reports=True,
        report_title='Test Suite',
        report_name='Jules App Test Report'
    )

    runner.run(smoke_test)