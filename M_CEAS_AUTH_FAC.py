"""
CEAS Mapping: M_CEAS_AUTH_FAC
Source: CEAS_WCDW.MVW_WCDW_AUTH_FAC -> Target: STAGE_EXT.CEAS_ACT_EXT_AUTH_FAC
"""

import sys
import os
from datetime import datetime
sys.path.append('/Workspace/Shared/BUNDLES/wcdw_project/common_utility')
from key_vault_configs import *
from common_functions import *
from common_notebook import *

sys.path.append("/Workspace/Shared/BUNDLES/wcdw_project/wcdw_workflows/WF_CEAS/ceas_common_notebook")
from wf_ceas_common_notebook import run_ceas_etl

# # Initialize Spark session
# spark = SparkSession.builder \
#     .appName("WF_CEAS_Migration") \
#     .config("spark.sql.legacy.timeParserPolicy", "LEGACY") \
#     .getOrCreate()


# # Initialize ADLS logger
# # TODO: Update log_path once adls_config is configured in key_vault_configs.py
# logger = ADLSLogger(
#     spark=spark,
#     log_path="need to updated",
#     workflow_name="WF_CEAS"
# )

workflow_start = datetime.now()
workflow_name = "WF_CEAS"
# adls_logger.info(f"=" * 80)
# adls_logger.info(f"Workflow {workflow_name} started at {workflow_start.isoformat()}")
# adls_logger.info(f"=" * 80)
session_name = "S_M_CEAS_AUTH_FAC"
mapping_name = "M_CEAS_AUTH_FAC"

query = """
(
    SELECT * FROM CEAS_WCDW.MVW_WCDW_AUTH_FAC
)
"""

column_mapping = [
        ("TDR_IND", "TDR_IND"),
        ("RISKMANAGER_NAME", "RISK_MANAGER_NAME"),
        ("RISK_MANAGER_REGION", "RISK_MANAGER_REGION"),
        ("LGD_OFFLINE_MODEL_ID", "LGD_OFFLINE_MODEL_ID"),
        ("LTV_RATIO", "LTV_RATIO"),
        ("MONITORING_SYSTEM_CODE", "MONITORING_SYSTEM_CODE"),
        ("LGD_ASSESSMENT_ID", "LGD_ASSESSMENT_ID"),
        ("PRIM_BOR_ASSET_CATEGORY_CODE", "PRIM_BOR_ASSET_CATEGORY_CODE"),
        ("PRIM_BOR_CUSTOMER_TYPE", "PRIM_BOR_CUSTOMER_TYPE"),
        ("PRIM_BOR_SA_FI_BANK_IND", "PRIM_BOR_SA_FI_BANK_IND"),
        ("PRIM_BOR_SCRA_GRADE", "PRIM_BOR_SCRA_GRADE"),
        ("FIRB_LGD_ASSMT_REF_ID", "FIRB_LGD_ASSMT_REF_ID"),
        ("FIRB_ELIGIBLE_IND", "FIRB_ELIGIBLE_IND"),
        ("FINAL_FIRB_LGD_RATING", "FINAL_FIRB_LGD_RATING"),
        ("ADC_RRE_IND", "ADC_RRE_IND"),
        ("PRIM_BOR_TOT_GAS_AMT_EXEDS_IND", "PRIM_BOR_TOT_GAS_AMT_EXEDS_IND"),
        ("FACILITY_DISPOSITION_CODE", "FACILITY_DISPOSITION_CODE"),
        ("PRIMARY_OBLIGOR_CUST_ID", "PRIMARY_OBLIGOR_CUST_ID"),
        ("PRIMARY_GUARNTR_CUST_SYSTEM_ID", "PRIMARY_GUARNTR_CUST_SYSTEM_ID"),
        ("PRIMARY_OBLIGOR_CUST_SYSTEM_ID", "PRIMARY_OBLIGOR_CUST_SYSTEM_ID"),
        ("PRIMARY_BORROWR_CUST_ID", "PRIMARY_BORROWR_CUST_ID"),
        ("PRIMARY_BORROWR_CUST_SYSTEM_ID", "PRIMARY_BORROWR_CUST_SYSTEM_ID"),
        ("PRIMARY_GUARNTR_CUST_ID", "PRIMARY_GUARNTR_CUST_ID"),
        ("LGD_ASSESSMENT_TYPE_ID", "LGD_ASSESSMENT_TYPE_ID"),
        ("APPROVED_AMOUNT_IN_NATIVE_CCY", "APPROVED_AMOUNT_IN_NATIVE_CCY"),
        ("SOVEREIGN_INDICATOR", "SOVEREIGN_INDICATOR"),
        ("REA_SIC_CODE", "REA_SIC_CODE"),
        ("REA_PROPERTY_TYPE_CODE", "REA_PROPERTY_TYPE_CODE"),
        ("REA_FINANCING_TYPE_CODE", "REA_FINANCING_TYPE_CODE"),
        ("ENTERPRISE_VALUE_DATE", "ENTERPRISE_VALUE_DATE"),
        ("FACILITY_ODR_BEFORE_GUARANTEE", "FACILITY_ODR_BEFORE_GUARANTEE"),
        ("FACILITY_CURRENCY_CODE", "FACILITY_CURRENCY_CODE"),
        ("CREDIT_APPLICATION_ID", "CREDIT_APPLICATION_ID"),
        ("AUTHORIZED_FACILITY_ID", "AUTHORIZED_FACILITY_ID"),
        ("AUTHORIZED_FACILITY_SYSTEM_ID", "AUTHORIZED_FACILITY_SYSTEM_ID"),
        ("COMMITMENT_TYPE_CODE", "COMMITMENT_TYPE_CODE"),
        ("FACILITY_FLR", "FACILITY_FLR"),
        ("FACILITY_LGD_RR", "FACILITY_LGD_RR"),
        ("FACILITY_ODR_AFTER_GUARANTEE", "FACILITY_ODR_AFTER_GUARANTEE"),
        ("FACILITY_STATUS_CODE", "FACILITY_STATUS_CODE"),
        ("FACILITY_TYPE_CODE", "FACILITY_TYPE_CODE"),
        ("LGD_ASSESSMENT_SYSTEM_ID", "LGD_ASSESSMENT_SYSTEM_ID"),
        ("LGD_ASSESSMENT_COMMON_CCY_CODE", "LGD_ASSESSMENT_COMMON_CCY_CODE"),
        ("MONITORING_SYSTEM_FACILITY_ID", "MONITORING_SYSTEM_FACILITY_ID"),
        ("PUBLIC_SECTOR_ENTITY_INDICATOR", "PUBLIC_SECTOR_ENTITY_INDICATOR"),
        ("RISK_COUNTRY_CODE", "RISK_COUNTRY_CODE"),
        ("SECURED_INDICATOR", "SECURED_INDICATOR"),
        ("SENIORITY_RANKING_CODE", "SENIORITY_RANKING_CODE"),
        ("SUBSTITUTED_GUARANTOR_SYSTE_ID", "SUBSTITUTED_GUARANTOR_SYSTE_ID"),
        ("SMALLEST_ENTERPRISE_VALUE_AMT", "SMALLEST_ENTERPRISE_VALUE_AMT"),
        ("SPECIALIZED_CATEGORY", "SPECIALIZED_CATEGORY"),
        ("SUBSTITUTED_GUARANTOR_ID", "SUBSTITUTED_GUARANTOR_ID"),
        ("LGD_BELOW_FLOOR_IND", "LGD_BELOW_FLOOR_IND"),
        ("LGD_FLOOR_VALUE", "LGD_FLOOR_VALUE"),
        ("MEMO_EXPOSURE_INDICATOR", "MEMO_EXPOSURE_INDICATOR"),
        ("CREDIT_APPLICATION_SYSTEM_ID", "CREDIT_APPLICATION_SYSTEM_ID"),
        ("EFFECTIVE_DATE_AUTHORIZATION", "EFFECTIVE_DATE_AUTHORIZATION"),
        ("AUTH_FAC_RISK_COUNTRY_CD", "AUTH_FAC_RISK_COUNTRY_CD"),
        ("RISK_MANAGER_ID", "RISK_MANAGER_ID"),
        ("DEBT_CLASSIFICATION_TYPE_CODE", "DEBT_CLASSIFICATION_TYPE_CODE"),
        ("CIBC_SHARE_LIEN_DEBT_PCT", "CIBC_SHARE_LIEN_DEBT_PCT"),
        ("DEBT_SOLD_IND", "DEBT_SOLD_IND")
        ]

run_ceas_etl(
    spark=spark,
    session_name=session_name,
    mapping_name=mapping_name,
    jdbc_url=jdbc_url,
    connection_properties=connection_properties,
    source_query=query,   # OR use source_table instead
    column_mapping=column_mapping,
    target_schema="STAGE_EXT",
    target_table="CEAS_ACT_EXT_AUTH_FAC",
    # partition_col="column name",   # optional
    # num_partitions=4,
    logger=logger
)
