import argparse
import sys
from src.config import logger
from src.ingestion import ingest_raw_excel
from src.transformation import transform_retail_data
from src.loader import load_staging_table
from src.sql_runner import execute_all_sql_scripts
from src.database import check_connection

def main():
    parser = argparse.ArgumentParser(
        description="Retail Data Engineering & Analytics Pipeline Orchestrator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py run-all       Run full end-to-end pipeline (ingest -> transform -> load -> sql)
  python main.py ingest        Ingest raw Excel dataset into raw CSV tier
  python main.py transform     Transform & clean raw CSV dataset
  python main.py load          Stage clean dataset into PostgreSQL
  python main.py sql           Execute Star Schema & Analytics View DDL/DML SQL scripts
  python main.py check-db      Verify database connection
        """
    )

    parser.add_argument(
        "action",
        choices=["ingest", "transform", "load", "sql", "run-all", "check-db"],
        help="Pipeline stage to execute"
    )

    args = parser.parse_args()

    try:
        if args.action == "check-db":
            logger.info("Checking database connection...")
            if check_connection():
                logger.info("Database connection SUCCESSFUL!")
            else:
                logger.error("Database connection FAILED. Please verify .env settings.")
                sys.exit(1)

        elif args.action == "ingest":
            ingest_raw_excel()

        elif args.action == "transform":
            transform_retail_data()

        elif args.action == "load":
            load_staging_table()

        elif args.action == "sql":
            execute_all_sql_scripts()

        elif args.action == "run-all":
            logger.info("==================================================")
            logger.info("STARTING END-TO-END RETAIL DATA ENGINEERING PIPELINE")
            logger.info("==================================================")
            
            logger.info("Stage 1/4: Data Ingestion")
            ingest_raw_excel()

            logger.info("Stage 2/4: Data Transformation")
            transform_retail_data()

            if check_connection():
                logger.info("Stage 3/4: Loading to Database Staging")
                load_staging_table()

                logger.info("Stage 4/4: Executing Warehouse SQL & Analytics Views")
                execute_all_sql_scripts()
                
                logger.info("==================================================")
                logger.info("PIPELINE EXECUTION COMPLETED SUCCESSFULLY!")
                logger.info("==================================================")
            else:
                logger.warning("Database not accessible. Ingestion and Transformation completed successfully. Skipping database loading.")
                logger.info("To run database stage later, setup PostgreSQL credentials in .env and run 'python main.py load'")

    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
