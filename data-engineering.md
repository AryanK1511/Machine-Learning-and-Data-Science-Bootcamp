# Data Engineering
At a very high level, a data engineer takes all the incoming data points from different sources and produces it and maintains it in databases or computers so that the company has access to this data.

#### What is Data?
- Data is information collected and stored on computers.
- In today's world, data is immensely valuable, with companies like Facebook and Google leveraging it for profit.
- Businesses use data to improve products, monitor performance, and identify areas for improvement.

#### Why Businesses Care About Data
- Data is a valuable asset for businesses, driving product improvement and revenue generation.
- Companies use data to create features like recommendation engines and monitor sales statistics.
- Data helps businesses assess their performance and identify opportunities for enhancement.

### Types of Data

#### 1. Structured Data
- Well-organized data typically stored in tables.
- Attributes are columns, rows are instances, often sourced from relational databases (e.g., MySQL).

#### 2. Semi-Structured Data
- Structured but stored in various formats like XML, CSV, or JSON.
- Examples from Kaggle show XML and JSON formats, with different structures for data organization.

#### 3. Unstructured Data
- Not easily analyzable due to complex formats.
- Examples include emails, PDFs, and other documents.

#### 4. Binary Data
- Files like audio, image, and video stored in binary (ones and zeros).
- Difficult for human analysis but comprehensible to computers.

### Data Engineer's Role
- Data engineers work on organizing and manipulating diverse data types.
- They integrate structured, semi-structured, unstructured, and binary data for effective business use.

**Note:**
- Businesses' increasing reliance on data underscores the importance of data engineers in managing and extracting value from different data sources.
- The variety of data types highlights the complexity of the data landscape and the need for skilled professionals to navigate it.

### Key Concepts:

#### 1. Data Mining
- **Definition:** Pre-processing and extracting knowledge from data.
- **Purpose:** Extract meaningful insights from raw data.

### 2. Big Data
- **Definition:** Large datasets that are too extensive to be processed on a single computer.
- **Challenge:** Requires cloud computing or distributed systems (e.g., AWS, Azure, Google Cloud) due to the sheer volume of data.
- **Technologies:** Hadoop, NoSQL.

### 3. Data Pipeline
- **Definition:** A system or process built by data engineers to manage the flow of data from various sources to useful forms.
- **Purpose:** Enable the extraction of valuable information from a vast amount of data.

### What Data Engineers Do:

- **Data Engineers:**
  - **Data Pipeline Creation:** Build pipelines to accumulate data from diverse sources (IoT devices, mobile apps, web apps, etc.).
  - **Database Management:** Organize and store data efficiently using databases and storage engines.
  - **Enable Data Utilization:** Facilitate data scientists, machine learning experts, and analysts by providing well-organized data for modeling and analysis.
  - **Support Business Decisions:** Assist in making informed business decisions through data insights.
  - **Foundation for Data Science:** Lay the groundwork for data scientists to focus on modeling by handling the data collection and organization.

### Significance of Data Engineers:

- **Critical Role:** Data engineers are crucial for setting the stage for data science activities within a company.
- **Data Collection:** They handle the initial stages of data collection, allowing data scientists to focus on modeling and analysis.
- **Data Pipeline Creation:** Build systems that transform raw data into a usable format, forming the foundation for various business applications.

### Data Engineering Tools:

#### 1. Apache Kafka
- **Function:** Collects data streams and facilitates their storage in data lakes.

#### 2. Data Lakes:
- **Examples:** Hadoop, Amazon S3, Azure Data Lake.
- **Purpose:** Store large volumes of raw data for further processing.

#### 3. Data Warehouses:
- **Examples:** Google BigQuery, Amazon Redshift, Amazon Athena.
- **Function:** Analyze structured data for business intelligence and reporting.

### Roles in the Data Flow:

#### 1. Software Engineer:
- **Responsibility:** Builds programs, apps, or systems that generate and release data.

#### 2. Data Engineer:
- **Responsibility:** Creates pipelines to ingest, process, and store data in data lakes and data warehouses.

#### 3. Data Scientist/Machine Learning Expert:
- **Data Usage:** Works with data lakes, extracting data for machine learning models.
- **Purpose:** Derives insights, builds models, and delivers business value.

#### 4. Data Analyst/Business Intelligence:
- **Data Usage:** Utilizes data warehouses and structured data for analysis and visualization.
- **Purpose:** Derives business value through structured data analysis.

### Data Flow in a Company:

1. **Data Generation:**
   - **By:** Software Engineers (app developers, mobile developers).
   - **Outcome:** Release of data through programs and applications.

2. **Data Engineering:**
   - **By:** Data Engineers.
   - **Function:** Ingests, processes, and stores data using tools like Apache Kafka, Hadoop, or data lakes.

3. **Data Science:**
   - **By:** Data Scientists/Machine Learning Experts.
   - **Data Source:** Data lakes.
   - **Outcome:** Extraction of valuable insights, model building for business value.

4. **Data Analysis/Business Intelligence:**
   - **By:** Data Analysts/Business Intelligence Professionals.
   - **Data Source:** Data warehouses.
   - **Outcome:** Structured data analysis, visualization, and business value derivation.

#### Key Tasks of a Data Engineer

#### 1. ETL Pipeline Building:
- **Definition:** ETL stands for Extract, Transform, Load.
- **Process:**
  - Extract: Data engineer extracts raw data generated by various systems.
  - Transform: Data is transformed into a usable form for loading into a data warehouse.
  - Load: Processed data is loaded into a data warehouse for company-wide use.
- **Programming Languages:** Python, Go, Scala, Java.

#### 2. Building Analysis Tools:
- **Purpose:** Ensure efficient monitoring and analysis of data and system health.
- **Tools:** Data engineers create tools for data scientists, analysts, and business intelligence professionals to analyze data and monitor system performance.

#### 3. Maintenance of Data Warehouse and Data Lakes:
- **Responsibility:** Ensure accessibility and functionality of data in data warehouses and data lakes.
- **Key Tasks:** Regular maintenance, optimization, and troubleshooting.

### Overview of Data Engineering Tools

#### Note to Learners:
- The following overview provides a general understanding of key tools in the data engineering landscape. The field is dynamic, with new tools emerging, so continued exploration is recommended.

#### Main Tools:
1. **Hadoop:**
   - **Function:** Distributed storage and processing of large datasets.
   - **Use Case:** Handling big data in distributed environments.

2. **Kafka:**
   - **Function:** Distributed event streaming platform.
   - **Use Case:** Ingesting, processing, and managing real-time data streams.

3. **Apache Spark:**
   - **Function:** Unified analytics engine for big data processing.
   - **Use Case:** Batch processing, real-time data processing, machine learning.

### Types of Databases:

#### 1. Relational Databases:
- **Definition:** Original type of database (e.g., PostgreSQL, MySQL).
- **Characteristics:** Uses SQL for transactions, strong consistency guarantees.
- **Limitations:** Challenges with distributed databases as data scales.

#### 2. NoSQL Databases:
- **Examples:** MongoDB.
- **Purpose:** Address the need for distributed databases, especially as data scales.
- **Characteristics:** Flexible, suitable for unstructured or semi-structured data.

#### 3. NewSQL Databases:
- **Examples:** VoltDB, CockroachDB.
- **Purpose:** Aim to combine benefits of both relational and NoSQL databases.
- **Characteristics:** Distributed nature for scalability, with ACID transaction guarantees.

### Databases for Specific Needs:

#### 1. Search Databases:
- **Examples:** Elasticsearch, Solr.
- **Purpose:** Designed for efficient and fast search capabilities.

#### 2. Computational Databases:
- **Examples:** Apache Spark.
- **Purpose:** Enables computation and analysis on data stored in databases.

### OLTP and OLAP Databases:

#### 1. OLTP (Online Transaction Processing) Databases:
- **Characteristics:** Used for transactional purposes (e.g., user interactions in web apps).
- **Example:** Relational databases.

#### 2. OLAP (Online Analytical Processing) Databases:
- **Characteristics:** Used for analytical purposes, supporting complex queries and reporting.
- **Example:** Data warehouses.

### Why Many Databases Exist:
- **Diverse Needs:** Different databases cater to specific requirements and use cases.
- **Evolution of Data Storage:** As data grew, the need for distributed databases emerged.
- **Specialized Functions:** Databases tailored for searches, computations, and analytical purposes.

### What is a Database?

- A **database** is a collection of data organized in a way that makes data management efficient.
- **Purpose:** Allows storage, retrieval, modification, and deletion of data.

### Database Management System (DBMS):

- A **DBMS** (Database Management System) is a collection of programs enabling access to and manipulation of databases.
- **Functionality:**
  - Allows users to interact with databases.
  - Controls user access to the database.

### Types of DBMS:

#### 1. Relational Database Management System (RDBMS):

- **Examples:** PostgreSQL, MySQL, Oracle, SQL Server.
- **Characteristics:**
  - Follows a structured format.
  - Comprises tables with columns and rows.
  - Requires a predefined schema.
  - Utilizes SQL (Structured Query Language) for communication.

#### 2. NoSQL Database:

- **Examples:** MongoDB, CouchDB, HyperTable.
- **Characteristics:**
  - Supports flexible data models.
  - Allows dynamic schema definition.
  - Suitable for unstructured or semi-structured data.
  - Diverse types: document-oriented (e.g., MongoDB), key-value stores, graph databases.

### Choosing Between Relational and NoSQL Databases:

- **Relational Databases:**
  - Suitable when data requirements are clear from the project's outset.
  - Well-structured, with defined schemas.
  - Commonly used in scenarios with structured data.

- **NoSQL Databases:**
  - Offers flexibility for projects with unclear or evolving data requirements.
  - Supports dynamic schema definition.
  - Suitable for projects dealing with unstructured or semi-structured data.

### Query Languages:

- **Relational Databases:** Use SQL (Structured Query Language) for communication.
- **NoSQL Databases:** Have their own query languages (e.g., MongoDB Query Language).

### Visualizing Storage Models:

#### 1. Relational Database Storage Model:
   - Tables linked by foreign keys.
   - Information stored in separate tables.

#### 2. NoSQL Database Storage Model (MongoDB Example):
   - Document-oriented storage.
   - Each document contains related information.

### Evolution of Data Storage Challenges

- **Challenge:** As companies generated more data, traditional databases (e.g., MySQL) became inefficient for handling large amounts of data.
- **Solution:** Hadoop, an open-source distributed processing framework, emerged as a cornerstone of data engineering.

### Hadoop Overview

- **Purpose:** Data processing and storage for big data.
- **Development:** Initially developed by Yahoo! and later donated to the Apache Software Foundation.
- **Key Components:**
  1. **Hadoop Distributed File System (HDFS):**
     - Allows storage of large amounts of data across multiple computers (scalability).
  2. **MapReduce:**
     - Enables batch processing of data using languages like Java or Python.

### Hadoop's Role

- **Data Lake Solution:**
  - Hadoop serves as a data lake, allowing the storage of massive amounts of data.

### Key Components Explained

1. **Hadoop Distributed File System (HDFS):**
   - **Purpose:** Scalable file system for storing large datasets.
   - **Scalability:** Data is distributed across different physical computers.
   - **Characteristic:** Enables the storage of petabytes of data efficiently.

2. **MapReduce:**
   - **Functionality:**
     - Performs batch processing on large datasets.
     - Executes jobs to clean, process, and analyze data.
   - **Language Support:** Primarily used with languages like Java or Python.
   - **Evolution:** Although effective, MapReduce usage has decreased with the emergence of faster alternatives like Apache Spark.

### Hive - SQL Interface for Hadoop

- **Purpose:** Makes the Hadoop cluster feel like a relational database.
- **Functionality:**
  - Allows users to write SQL queries against data stored in HDFS.
  - Provides a SQL-like interface for interacting with Hadoop.

### Hadoop in Data Engineering

- **Data Engineer's Role:**
  - Works behind the scenes to build systems for data collection, ETL jobs (Extract, Transform, Load), and large-scale data processing.
  - Hadoop serves as a storage layer for large datasets and facilitates batch processing.

### Evolution from Hadoop to Apache Spark

- **Background:**
  - Hadoop and MapReduce were initially used for batch processing in data engineering.
  - Apache Spark emerged as an improvement over Hadoop and MapReduce.
- **Apache Spark Advancements:**
  - Introduced in-memory processing, significantly enhancing processing speed.
  - Became a go-to batch processing framework for data engineers.

### Apache Spark Overview

- **Purpose:**
  - Batch processing framework for ETL (Extract, Transform, Load) jobs.
  - Efficiently processes large volumes of data.
- **Key Features:**
  - **In-Memory Processing:**
    - Allows Spark to run processing jobs much faster than traditional MapReduce.
  - **Compatibility:**
    - Works seamlessly with Hadoop, allowing data stored in HDFS to be processed.

### Real-Time Processing with Streaming

- **Shift from Batch Processing to Real-Time Processing:**
  - Traditional batch processing involved processing chunks of data over time.
  - **Real-Time Processing:**
    - Spark Streaming introduced the concept of processing data as it arrives, enabling real-time insights.

### Apache Flink - Real-Time Stream Processing

- **Introduction:**
  - Apache Flink focuses on real-time stream processing.
  - Offers an alternative to Spark Streaming.
- **Key Features:**
  - **Real-Time Processing:**
    - Processes data as it arrives, providing low-latency stream processing.
  - **Versatility:**
    - Suitable for both batch and stream processing workloads.

### Recap: Data Ingestion and Storage

- **Data Engineering Overview:**
  - Collecting and ingesting data.
  - Storing data in a data lake, often utilizing Hadoop clusters or object storage like Amazon S3.
  - Batch jobs are traditionally used to process and clean the data.

### Real-Time Stream Processing

- **Evolution in Data Processing:**
  - Shift from batch processing to real-time stream processing.
  - Faster reactions to data with real-time processing.

### Apache Kafka: Distributed Streaming Platform

- **Introduction to Kafka:**
  - Kafka is a distributed streaming platform.
  - Allows reading, writing, processing, and storing streams of data.
  - Acts as a messaging system for data.

### Kafka in Data Engineering Landscape

- **Central Role of Kafka:**
  - Kafka serves as a central hub for receiving messages, logs, and data from various sources.
  - Routes data to different destinations based on processing needs.

### Stream Processing Tools

- **Real-Time Processing Tools:**
  - Apache Spark Streaming
  - Apache Flink
  - Apache Storm
  - Amazon Kinesis

### Collaborative Role of Data Engineers

- **Collaboration Between Data Engineers and Data Scientists:**
  - Data engineers set up the landscape for data scientists.
  - Ingest data through Kafka, store in Hadoop or Amazon S3, process with Apache Spark or other tools.
  - Create a structured environment for data analysis and machine learning.