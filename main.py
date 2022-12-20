from processor.dataprocessor_service import DataProcessorService


"""
    Main-модуль, т.е. модуль запуска приложений ("точка входа" приложения)
"""


if __name__ == '__main__':
    service = DataProcessorService(datasource="productsData.txt", db_connection_url="sqlite:///test.db")
    service.run_service()
