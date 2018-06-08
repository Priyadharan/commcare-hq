# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0049_icdsauditentryrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='AggAwc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.TextField()),
                ('district_id', models.TextField()),
                ('block_id', models.TextField()),
                ('supervisor_id', models.TextField()),
                ('awc_id', models.TextField()),
                ('month', models.DateField()),
                ('num_awcs', models.SmallIntegerField()),
                ('awc_days_open', models.SmallIntegerField(null=True)),
                ('total_eligible_children', models.SmallIntegerField(null=True)),
                ('total_attended_children', models.SmallIntegerField(null=True)),
                ('pse_avg_attendance_percent', models.DecimalField(decimal_places=20, max_digits=64, null=True)),
                ('pse_full', models.IntegerField(null=True)),
                ('pse_partial', models.IntegerField(null=True)),
                ('pse_non', models.IntegerField(null=True)),
                ('pse_score', models.DecimalField(decimal_places=20, max_digits=64, null=True)),
                ('awc_days_provided_breakfast', models.IntegerField(null=True)),
                ('awc_days_provided_hotmeal', models.IntegerField(null=True)),
                ('awc_days_provided_thr', models.IntegerField(null=True)),
                ('awc_days_provided_pse', models.IntegerField(null=True)),
                ('awc_not_open_holiday', models.IntegerField(null=True)),
                ('awc_not_open_festival', models.IntegerField(null=True)),
                ('awc_not_open_no_help', models.IntegerField(null=True)),
                ('awc_not_open_department_work', models.IntegerField(null=True)),
                ('awc_not_open_other', models.IntegerField(null=True)),
                ('awc_num_open', models.IntegerField(null=True)),
                ('awc_not_open_no_data', models.IntegerField(null=True)),
                ('wer_weighed', models.IntegerField(null=True)),
                ('wer_eligible', models.IntegerField(null=True)),
                ('wer_score', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('thr_eligible_child', models.IntegerField(null=True)),
                ('thr_rations_21_plus_distributed_child', models.IntegerField(null=True)),
                ('thr_eligible_ccs', models.IntegerField(null=True)),
                ('thr_rations_21_plus_distributed_ccs', models.IntegerField(null=True)),
                ('thr_score', models.DecimalField(decimal_places=20, max_digits=64, null=True)),
                ('awc_score', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('num_awc_rank_functional', models.IntegerField(null=True)),
                ('num_awc_rank_semi', models.IntegerField(null=True)),
                ('num_awc_rank_non', models.IntegerField(null=True)),
                ('cases_ccs_pregnant', models.IntegerField(null=True)),
                ('cases_ccs_lactating', models.IntegerField(null=True)),
                ('cases_child_health', models.IntegerField(null=True)),
                ('usage_num_pse', models.IntegerField(null=True)),
                ('usage_num_gmp', models.IntegerField(null=True)),
                ('usage_num_thr', models.IntegerField(null=True)),
                ('usage_num_home_visit', models.IntegerField(null=True)),
                ('usage_num_bp_tri1', models.IntegerField(null=True)),
                ('usage_num_bp_tri2', models.IntegerField(null=True)),
                ('usage_num_bp_tri3', models.IntegerField(null=True)),
                ('usage_num_pnc', models.IntegerField(null=True)),
                ('usage_num_ebf', models.IntegerField(null=True)),
                ('usage_num_cf', models.IntegerField(null=True)),
                ('usage_num_delivery', models.IntegerField(null=True)),
                ('usage_num_due_list_ccs', models.IntegerField(null=True)),
                ('usage_num_due_list_child_health', models.IntegerField(null=True)),
                ('usage_awc_num_active', models.IntegerField(null=True)),
                ('usage_time_pse', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('usage_time_gmp', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('usage_time_bp', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('usage_time_pnc', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('usage_time_ebf', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('usage_time_cf', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('usage_time_of_day_pse', models.TimeField(null=True)),
                ('usage_time_of_day_home_visit', models.TimeField(null=True)),
                ('vhnd_immunization', models.IntegerField(null=True)),
                ('vhnd_anc', models.IntegerField(null=True)),
                ('vhnd_gmp', models.IntegerField(null=True)),
                ('vhnd_num_pregnancy', models.IntegerField(null=True)),
                ('vhnd_num_lactating', models.IntegerField(null=True)),
                ('vhnd_num_mothers_6_12', models.IntegerField(null=True)),
                ('vhnd_num_mothers_12', models.IntegerField(null=True)),
                ('vhnd_num_fathers', models.IntegerField(null=True)),
                ('ls_supervision_visit', models.IntegerField(null=True)),
                ('ls_num_supervised', models.IntegerField(null=True)),
                ('ls_awc_location_long', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('ls_awc_location_lat', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('ls_awc_present', models.IntegerField(null=True)),
                ('ls_awc_open', models.IntegerField(null=True)),
                ('ls_awc_not_open_aww_not_available', models.IntegerField(null=True)),
                ('ls_awc_not_open_closed_early', models.IntegerField(null=True)),
                ('ls_awc_not_open_holiday', models.IntegerField(null=True)),
                ('ls_awc_not_open_unknown', models.IntegerField(null=True)),
                ('ls_awc_not_open_other', models.IntegerField(null=True)),
                ('infra_last_update_date', models.DateField(null=True)),
                ('infra_type_of_building', models.TextField(null=True)),
                ('infra_type_of_building_pucca', models.IntegerField(null=True)),
                ('infra_type_of_building_semi_pucca', models.IntegerField(null=True)),
                ('infra_type_of_building_kuccha', models.IntegerField(null=True)),
                ('infra_type_of_building_partial_covered_space', models.IntegerField(null=True)),
                ('infra_clean_water', models.IntegerField(null=True)),
                ('infra_functional_toilet', models.IntegerField(null=True)),
                ('infra_baby_weighing_scale', models.IntegerField(null=True)),
                ('infra_flat_weighing_scale', models.IntegerField(null=True)),
                ('infra_adult_weighing_scale', models.IntegerField(null=True)),
                ('infra_cooking_utensils', models.IntegerField(null=True)),
                ('infra_medicine_kits', models.IntegerField(null=True)),
                ('infra_adequate_space_pse', models.IntegerField(null=True)),
                ('cases_person_beneficiary', models.IntegerField(null=True)),
                ('cases_person_referred', models.IntegerField(null=True)),
                ('awc_days_pse_conducted', models.IntegerField(null=True)),
                ('num_awc_infra_last_update', models.IntegerField(null=True)),
                ('cases_person_has_aadhaar_v2', models.IntegerField(null=True)),
                ('cases_person_beneficiary_v2', models.IntegerField(null=True)),
                ('electricity_awc', models.IntegerField(null=True)),
                ('infantometer', models.IntegerField(null=True)),
                ('stadiometer', models.IntegerField(null=True)),
                ('num_anc_visits', models.IntegerField(null=True)),
                ('num_children_immunized', models.IntegerField(null=True)),
                ('usage_num_hh_reg', models.IntegerField(null=True)),
                ('usage_num_add_person', models.IntegerField(null=True)),
                ('usage_num_add_pregnancy', models.IntegerField(null=True)),
                ('is_launched', models.TextField(null=True)),
                ('training_phase', models.IntegerField(null=True)),
                ('trained_phase_1', models.IntegerField(null=True)),
                ('trained_phase_2', models.IntegerField(null=True)),
                ('trained_phase_3', models.IntegerField(null=True)),
                ('trained_phase_4', models.IntegerField(null=True)),
                ('aggregation_level', models.IntegerField(null=True)),
                ('num_launched_states', models.IntegerField(null=True)),
                ('num_launched_districts', models.IntegerField(null=True)),
                ('num_launched_blocks', models.IntegerField(null=True)),
                ('num_launched_supervisors', models.IntegerField(null=True)),
                ('num_launched_awcs', models.IntegerField(null=True)),
                ('cases_household', models.IntegerField(null=True)),
                ('cases_person', models.IntegerField(null=True)),
                ('cases_person_all', models.IntegerField(null=True)),
                ('cases_person_has_aadhaar', models.IntegerField(null=True)),
                ('cases_ccs_pregnant_all', models.IntegerField(null=True)),
                ('cases_ccs_lactating_all', models.IntegerField(null=True)),
                ('cases_child_health_all', models.IntegerField(null=True)),
                ('cases_person_adolescent_girls_11_14', models.IntegerField(null=True)),
                ('cases_person_adolescent_girls_15_18', models.IntegerField(null=True)),
                ('cases_person_adolescent_girls_11_14_all', models.IntegerField(null=True)),
                ('cases_person_adolescent_girls_15_18_all', models.IntegerField(null=True)),
                ('infra_infant_weighing_scale', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'agg_awc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AggAwcDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.TextField()),
                ('district_id', models.TextField()),
                ('block_id', models.TextField()),
                ('supervisor_id', models.TextField()),
                ('awc_id', models.TextField()),
                ('aggregation_level', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('cases_household', models.IntegerField(null=True)),
                ('cases_person', models.IntegerField(null=True)),
                ('cases_person_all', models.IntegerField(null=True)),
                ('cases_person_has_aadhaar', models.IntegerField(null=True)),
                ('cases_child_health', models.IntegerField(null=True)),
                ('cases_child_health_all', models.IntegerField(null=True)),
                ('cases_ccs_pregnant', models.IntegerField(null=True)),
                ('cases_ccs_pregnant_all', models.IntegerField(null=True)),
                ('cases_ccs_lactating', models.IntegerField(null=True)),
                ('cases_ccs_lactating_all', models.IntegerField(null=True)),
                ('cases_person_adolescent_girls_11_14', models.IntegerField(null=True)),
                ('cases_person_adolescent_girls_15_18', models.IntegerField(null=True)),
                ('cases_person_adolescent_girls_11_14_all', models.IntegerField(null=True)),
                ('cases_person_adolescent_girls_15_18_all', models.IntegerField(null=True)),
                ('daily_attendance_open', models.IntegerField(null=True)),
                ('num_awcs', models.IntegerField(null=True)),
                ('num_launched_states', models.IntegerField(null=True)),
                ('num_launched_districts', models.IntegerField(null=True)),
                ('num_launched_blocks', models.IntegerField(null=True)),
                ('num_launched_supervisors', models.IntegerField(null=True)),
                ('num_launched_awcs', models.IntegerField(null=True)),
                ('cases_person_beneficiary', models.IntegerField(null=True)),
                ('cases_person_has_aadhaar_v2', models.IntegerField(null=True)),
                ('cases_person_beneficiary_v2', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'agg_awc_daily',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AggCcsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.TextField()),
                ('district_id', models.TextField()),
                ('block_id', models.TextField()),
                ('supervisor_id', models.TextField()),
                ('awc_id', models.TextField()),
                ('month', models.DateField()),
                ('ccs_status', models.TextField()),
                ('trimester', models.TextField()),
                ('caste', models.TextField(null=True)),
                ('disabled', models.TextField(null=True)),
                ('minority', models.TextField(null=True)),
                ('resident', models.TextField(null=True)),
                ('valid_in_month', models.IntegerField()),
                ('lactating', models.IntegerField()),
                ('pregnant', models.IntegerField()),
                ('thr_eligible', models.IntegerField()),
                ('rations_21_plus_distributed', models.IntegerField()),
                ('tetanus_complete', models.IntegerField()),
                ('delivered_in_month', models.IntegerField()),
                ('anc1_received_at_delivery', models.IntegerField()),
                ('anc2_received_at_delivery', models.IntegerField()),
                ('anc3_received_at_delivery', models.IntegerField()),
                ('anc4_received_at_delivery', models.IntegerField()),
                ('registration_trimester_at_delivery', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('using_ifa', models.IntegerField()),
                ('ifa_consumed_last_seven_days', models.IntegerField()),
                ('anemic_normal', models.IntegerField()),
                ('anemic_moderate', models.IntegerField()),
                ('anemic_severe', models.IntegerField()),
                ('anemic_unknown', models.IntegerField()),
                ('extra_meal', models.IntegerField()),
                ('resting_during_pregnancy', models.IntegerField()),
                ('bp1_complete', models.IntegerField()),
                ('bp2_complete', models.IntegerField()),
                ('bp3_complete', models.IntegerField()),
                ('pnc_complete', models.IntegerField()),
                ('trimester_2', models.IntegerField()),
                ('trimester_3', models.IntegerField()),
                ('postnatal', models.IntegerField()),
                ('counsel_bp_vid', models.IntegerField()),
                ('counsel_preparation', models.IntegerField()),
                ('counsel_immediate_bf', models.IntegerField()),
                ('counsel_fp_vid', models.IntegerField()),
                ('counsel_immediate_conception', models.IntegerField()),
                ('counsel_accessible_postpartum_fp', models.IntegerField()),
                ('has_aadhar_id', models.IntegerField(null=True)),
                ('aggregation_level', models.IntegerField(null=True)),
                ('valid_all_registered_in_month', models.IntegerField(null=True)),
                ('institutional_delivery_in_month', models.IntegerField(null=True)),
                ('lactating_all', models.IntegerField(null=True)),
                ('pregnant_all', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'agg_ccs_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AggChildHealth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.TextField()),
                ('district_id', models.TextField()),
                ('block_id', models.TextField()),
                ('supervisor_id', models.TextField()),
                ('awc_id', models.TextField()),
                ('month', models.DateField()),
                ('gender', models.TextField(null=True)),
                ('age_tranche', models.TextField(null=True)),
                ('caste', models.TextField(null=True)),
                ('disabled', models.TextField(null=True)),
                ('minority', models.TextField(null=True)),
                ('resident', models.TextField(null=True)),
                ('valid_in_month', models.IntegerField()),
                ('nutrition_status_weighed', models.IntegerField()),
                ('nutrition_status_unweighed', models.IntegerField()),
                ('nutrition_status_normal', models.IntegerField()),
                ('nutrition_status_moderately_underweight', models.IntegerField()),
                ('nutrition_status_severely_underweight', models.IntegerField()),
                ('wer_eligible', models.IntegerField()),
                ('thr_eligible', models.IntegerField()),
                ('rations_21_plus_distributed', models.IntegerField()),
                ('pse_eligible', models.IntegerField()),
                ('pse_attended_16_days', models.IntegerField()),
                ('born_in_month', models.IntegerField()),
                ('low_birth_weight_in_month', models.IntegerField()),
                ('bf_at_birth', models.IntegerField()),
                ('ebf_eligible', models.IntegerField()),
                ('ebf_in_month', models.IntegerField()),
                ('cf_eligible', models.IntegerField()),
                ('cf_in_month', models.IntegerField()),
                ('cf_diet_diversity', models.IntegerField()),
                ('cf_diet_quantity', models.IntegerField()),
                ('cf_demo', models.IntegerField()),
                ('cf_handwashing', models.IntegerField()),
                ('counsel_increase_food_bf', models.IntegerField()),
                ('counsel_manage_breast_problems', models.IntegerField()),
                ('counsel_ebf', models.IntegerField()),
                ('counsel_adequate_bf', models.IntegerField()),
                ('counsel_pediatric_ifa', models.IntegerField()),
                ('counsel_play_cf_video', models.IntegerField()),
                ('fully_immunized_eligible', models.IntegerField()),
                ('fully_immunized_on_time', models.IntegerField()),
                ('fully_immunized_late', models.IntegerField()),
                ('weighed_and_height_measured_in_month', models.IntegerField(null=True)),
                ('weighed_and_born_in_month', models.IntegerField(null=True)),
                ('days_ration_given_child', models.IntegerField(null=True)),
                ('zscore_grading_hfa_normal', models.IntegerField(null=True)),
                ('zscore_grading_hfa_moderate', models.IntegerField(null=True)),
                ('zscore_grading_hfa_severe', models.IntegerField(null=True)),
                ('wasting_normal_v2', models.IntegerField(null=True)),
                ('wasting_moderate_v2', models.IntegerField(null=True)),
                ('wasting_severe_v2', models.IntegerField(null=True)),
                ('has_aadhar_id', models.IntegerField(null=True)),
                ('aggregation_level', models.IntegerField(null=True)),
                ('pnc_eligible', models.IntegerField(null=True)),
                ('height_eligible', models.IntegerField(null=True)),
                ('wasting_moderate', models.IntegerField(null=True)),
                ('wasting_severe', models.IntegerField(null=True)),
                ('stunting_moderate', models.IntegerField(null=True)),
                ('stunting_severe', models.IntegerField(null=True)),
                ('cf_initiation_in_month', models.IntegerField(null=True)),
                ('cf_initiation_eligible', models.IntegerField(null=True)),
                ('height_measured_in_month', models.IntegerField(null=True)),
                ('wasting_normal', models.IntegerField(null=True)),
                ('stunting_normal', models.IntegerField(null=True)),
                ('valid_all_registered_in_month', models.IntegerField(null=True)),
                ('ebf_no_info_recorded', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'agg_child_health',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CcsRecordMonthly',
            fields=[
                ('awc_id', models.TextField()),
                ('case_id', models.TextField(primary_key=True, serialize=False)),
                ('month', models.DateField()),
                ('age_in_months', models.IntegerField(blank=True, null=True)),
                ('ccs_status', models.TextField(blank=True, null=True)),
                ('open_in_month', models.IntegerField(blank=True, null=True)),
                ('alive_in_month', models.IntegerField(blank=True, null=True)),
                ('trimester', models.IntegerField(blank=True, null=True)),
                ('num_rations_distributed', models.IntegerField(blank=True, null=True)),
                ('thr_eligible', models.IntegerField(blank=True, null=True)),
                ('tetanus_complete', models.IntegerField(blank=True, null=True)),
                ('delivered_in_month', models.IntegerField(blank=True, null=True)),
                ('anc1_received_at_delivery', models.IntegerField(blank=True, null=True)),
                ('anc2_received_at_delivery', models.IntegerField(blank=True, null=True)),
                ('anc3_received_at_delivery', models.IntegerField(blank=True, null=True)),
                ('anc4_received_at_delivery', models.IntegerField(blank=True, null=True)),
                ('registration_trimester_at_delivery', models.IntegerField(blank=True, null=True)),
                ('using_ifa', models.IntegerField(blank=True, null=True)),
                ('ifa_consumed_last_seven_days', models.IntegerField(blank=True, null=True)),
                ('anemic_severe', models.IntegerField(blank=True, null=True)),
                ('anemic_moderate', models.IntegerField(blank=True, null=True)),
                ('anemic_normal', models.IntegerField(blank=True, null=True)),
                ('anemic_unknown', models.IntegerField(blank=True, null=True)),
                ('extra_meal', models.IntegerField(blank=True, null=True)),
                ('resting_during_pregnancy', models.IntegerField(blank=True, null=True)),
                ('bp_visited_in_month', models.IntegerField(blank=True, null=True)),
                ('pnc_visited_in_month', models.IntegerField(blank=True, null=True)),
                ('trimester_2', models.IntegerField(blank=True, null=True)),
                ('trimester_3', models.IntegerField(blank=True, null=True)),
                ('counsel_immediate_bf', models.IntegerField(blank=True, null=True)),
                ('counsel_bp_vid', models.IntegerField(blank=True, null=True)),
                ('counsel_preparation', models.IntegerField(blank=True, null=True)),
                ('counsel_fp_vid', models.IntegerField(blank=True, null=True)),
                ('counsel_immediate_conception', models.IntegerField(blank=True, null=True)),
                ('counsel_accessible_postpartum_fp', models.IntegerField(blank=True, null=True)),
                ('bp1_complete', models.IntegerField(blank=True, null=True)),
                ('bp2_complete', models.IntegerField(blank=True, null=True)),
                ('bp3_complete', models.IntegerField(blank=True, null=True)),
                ('pnc_complete', models.IntegerField(blank=True, null=True)),
                ('postnatal', models.IntegerField(blank=True, null=True)),
                ('has_aadhar_id', models.IntegerField(blank=True, null=True)),
                ('counsel_fp_methods', models.IntegerField(blank=True, null=True)),
                ('pregnant', models.IntegerField(blank=True, null=True)),
                ('pregnant_all', models.IntegerField(blank=True, null=True)),
                ('lactating', models.IntegerField(blank=True, null=True)),
                ('lactating_all', models.IntegerField(blank=True, null=True)),
                ('institutional_delivery_in_month', models.IntegerField(blank=True, null=True)),
                ('add', models.DateField(blank=True, null=True)),
                ('anc_in_month', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ccs_record_monthly',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChildHealthMonthly',
            fields=[
                ('awc_id', models.TextField()),
                ('case_id', models.TextField(primary_key=True, serialize=False)),
                ('month', models.DateField()),
                ('age_in_months', models.IntegerField(blank=True, null=True)),
                ('open_in_month', models.IntegerField(blank=True, null=True)),
                ('alive_in_month', models.IntegerField(blank=True, null=True)),
                ('wer_eligible', models.IntegerField(blank=True, null=True)),
                ('nutrition_status_last_recorded', models.TextField(blank=True, null=True)),
                ('current_month_nutrition_status', models.TextField(blank=True, null=True)),
                ('nutrition_status_weighed', models.IntegerField(blank=True, null=True)),
                ('num_rations_distributed', models.IntegerField(blank=True, null=True)),
                ('pse_eligible', models.IntegerField(blank=True, null=True)),
                ('pse_days_attended', models.IntegerField(blank=True, null=True)),
                ('born_in_month', models.IntegerField(blank=True, null=True)),
                ('low_birth_weight_born_in_month', models.IntegerField(blank=True, null=True)),
                ('bf_at_birth_born_in_month', models.IntegerField(blank=True, null=True)),
                ('ebf_eligible', models.IntegerField(blank=True, null=True)),
                ('ebf_in_month', models.IntegerField(blank=True, null=True)),
                ('ebf_not_breastfeeding_reason', models.TextField(blank=True, null=True)),
                ('ebf_drinking_liquid', models.IntegerField(blank=True, null=True)),
                ('ebf_eating', models.IntegerField(blank=True, null=True)),
                ('ebf_no_bf_no_milk', models.IntegerField(blank=True, null=True)),
                ('ebf_no_bf_pregnant_again', models.IntegerField(blank=True, null=True)),
                ('ebf_no_bf_child_too_old', models.IntegerField(blank=True, null=True)),
                ('ebf_no_bf_mother_sick', models.IntegerField(blank=True, null=True)),
                ('cf_eligible', models.IntegerField(blank=True, null=True)),
                ('cf_in_month', models.IntegerField(blank=True, null=True)),
                ('cf_diet_diversity', models.IntegerField(blank=True, null=True)),
                ('cf_diet_quantity', models.IntegerField(blank=True, null=True)),
                ('cf_handwashing', models.IntegerField(blank=True, null=True)),
                ('cf_demo', models.IntegerField(blank=True, null=True)),
                ('fully_immunized_eligible', models.IntegerField(blank=True, null=True)),
                ('fully_immunized_on_time', models.IntegerField(blank=True, null=True)),
                ('fully_immunized_late', models.IntegerField(blank=True, null=True)),
                ('counsel_ebf', models.IntegerField(blank=True, null=True)),
                ('counsel_adequate_bf', models.IntegerField(blank=True, null=True)),
                ('counsel_pediatric_ifa', models.IntegerField(blank=True, null=True)),
                ('counsel_comp_feeding_vid', models.IntegerField(blank=True, null=True)),
                ('counsel_increase_food_bf', models.IntegerField(blank=True, null=True)),
                ('counsel_manage_breast_problems', models.IntegerField(blank=True, null=True)),
                ('counsel_skin_to_skin', models.IntegerField(blank=True, null=True)),
                ('counsel_immediate_breastfeeding', models.IntegerField(blank=True, null=True)),
                ('recorded_weight', models.DecimalField(blank=True, decimal_places=20, max_digits=64, null=True)),
                ('recorded_height', models.DecimalField(blank=True, decimal_places=20, max_digits=64, null=True)),
                ('has_aadhar_id', models.IntegerField(blank=True, null=True)),
                ('thr_eligible', models.IntegerField(blank=True, null=True)),
                ('pnc_eligible', models.IntegerField(blank=True, null=True)),
                ('cf_initiation_in_month', models.IntegerField(blank=True, null=True)),
                ('cf_initiation_eligible', models.IntegerField(blank=True, null=True)),
                ('height_measured_in_month', models.IntegerField(blank=True, null=True)),
                ('current_month_stunting', models.TextField(blank=True, null=True)),
                ('stunting_last_recorded', models.TextField(blank=True, null=True)),
                ('wasting_last_recorded', models.TextField(blank=True, null=True)),
                ('current_month_wasting', models.TextField(blank=True, null=True)),
                ('valid_in_month', models.IntegerField(blank=True, null=True)),
                ('valid_all_registered_in_month', models.IntegerField(blank=True, null=True)),
                ('ebf_no_info_recorded', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('sex', models.TextField(blank=True, null=True)),
                ('age_tranche', models.TextField(blank=True, null=True)),
                ('caste', models.TextField(blank=True, null=True)),
                ('disabled', models.TextField(blank=True, null=True)),
                ('minority', models.TextField(blank=True, null=True)),
                ('resident', models.TextField(blank=True, null=True)),
                ('person_name', models.TextField(blank=True, null=True)),
                ('mother_name', models.TextField(blank=True, null=True)),
                ('immunization_in_month', models.SmallIntegerField(blank=True, null=True)),
                ('days_ration_given_child', models.SmallIntegerField(blank=True, null=True)),
                ('zscore_grading_hfa', models.SmallIntegerField(blank=True, null=True)),
                ('zscore_grading_hfa_recorded_in_month', models.SmallIntegerField(blank=True, null=True)),
                ('zscore_grading_wfh', models.SmallIntegerField(blank=True, null=True)),
                ('zscore_grading_wfh_recorded_in_month', models.SmallIntegerField(blank=True, null=True)),
                ('muac_grading', models.SmallIntegerField(blank=True, null=True)),
                ('muac_grading_recorded_in_month', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'child_health_monthly',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DailyAttendance',
            fields=[
                ('doc_id', models.TextField(primary_key=True, serialize=False)),
                ('awc_id', models.TextField(null=True)),
                ('month', models.DateField(null=True)),
                ('pse_date', models.DateField(null=True)),
                ('awc_open_count', models.IntegerField(null=True)),
                ('count', models.IntegerField(null=True)),
                ('eligible_children', models.IntegerField(null=True)),
                ('attended_children', models.IntegerField(null=True)),
                ('attended_children_percent', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('form_location', models.TextField(null=True)),
                ('form_location_lat', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('form_location_long', models.DecimalField(decimal_places=16, max_digits=64, null=True)),
                ('image_name', models.TextField(null=True)),
            ],
            options={
                'db_table': 'daily_attendance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IcdsMonths',
            fields=[
                ('month_name', models.TextField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'icds_months',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='aggregateccsrecordpostnatalcareforms',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='aggregatechildhealthpostnatalcareforms',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='aggregatechildhealththrforms',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='aggregatecomplementaryfeedingforms',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='aggregategrowthmonitoringforms',
            options={'managed': False},
        ),
        migrations.AlterField(
            model_name='icdsauditentryrecord',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
