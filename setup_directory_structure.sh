#!/bin/bash

# Create main directory
mkdir -p ai_app_idea_generator

# Create subdirectories and files
mkdir -p ai_app_idea_generator/data_collection
touch ai_app_idea_generator/data_collection/google_trends_collector.py
touch ai_app_idea_generator/data_collection/social_media_collector.py
touch ai_app_idea_generator/data_collection/app_store_collector.py

mkdir -p ai_app_idea_generator/data_processing
touch ai_app_idea_generator/data_processing/data_cleaning.py
touch ai_app_idea_generator/data_processing/trend_analysis.py
touch ai_app_idea_generator/data_processing/keyword_extraction.py

mkdir -p ai_app_idea_generator/ai_generation
touch ai_app_idea_generator/ai_generation/prompt_engineering.py
touch ai_app_idea_generator/ai_generation/idea_generator.py
touch ai_app_idea_generator/ai_generation/idea_filtering.py

mkdir -p ai_app_idea_generator/idea_delivery
touch ai_app_idea_generator/idea_delivery/report_generation.py
touch ai_app_idea_generator/idea_delivery/notification_system.py

mkdir -p ai_app_idea_generator/ai_assisted_development/code_generation_tools
touch ai_app_idea_generator/ai_assisted_development/development_scripts.py

mkdir -p ai_app_idea_generator/feedback_iteration
touch ai_app_idea_generator/feedback_iteration/feedback_collection.py
touch ai_app_idea_generator/feedback_iteration/model_retraining.py

mkdir -p ai_app_idea_generator/tests
touch ai_app_idea_generator/tests/test_data_collection.py
touch ai_app_idea_generator/tests/test_data_processing.py
touch ai_app_idea_generator/tests/test_ai_generation.py

mkdir -p ai_app_idea_generator/config
touch ai_app_idea_generator/config/settings.py
touch ai_app_idea_generator/config/logging.conf

mkdir -p ai_app_idea_generator/scripts
touch ai_app_idea_generator/scripts/run_all.py
touch ai_app_idea_generator/scripts/schedule_tasks.py

mkdir -p ai_app_idea_generator/docs
touch ai_app_idea_generator/docs/README.md
touch ai_app_idea_generator/docs/requirements.txt

touch ai_app_idea_generator/requirements.txt
touch ai_app_idea_generator/README.md

# Move .gitignore to the correct location
mv .gitignore ai_app_idea_generator/.gitignore

echo "Directory structure created successfully!"
