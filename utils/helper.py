import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# ==========================================
# DATA LOADING
# ==========================================

def load_weather_data(path):
    """
    Load weather parquet dataset
    """
    df = pd.read_parquet(path)
    return df


def load_csv(path):
    """
    Load csv file
    """
    return pd.read_csv(path)


# ==========================================
# DATA SUMMARY
# ==========================================

def get_basic_info(df):

    info = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum()
    }

    return info


def get_numeric_columns(df):

    return df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()


# ==========================================
# KPI CALCULATIONS
# ==========================================

def get_kpis(df):

    numeric_cols = get_numeric_columns(df)

    if len(numeric_cols) == 0:
        return {}

    kpis = {
        "Total Records": len(df),
        "Features": len(df.columns),
        "Avg Value": round(
            df[numeric_cols].mean().mean(),
            2
        ),
        "Max Value": round(
            df[numeric_cols].max().max(),
            2
        )
    }

    return kpis


# ==========================================
# MISSING VALUES
# ==========================================

def missing_values_table(df):

    missing = pd.DataFrame(
        {
            "Column": df.columns,
            "Missing": df.isnull().sum().values
        }
    )

    missing = missing.sort_values(
        by="Missing",
        ascending=False
    )

    return missing


# ==========================================
# OUTLIER DETECTION
# ==========================================

def detect_outliers(df, column):

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - (1.5 * IQR)
    upper = Q3 + (1.5 * IQR)

    outliers = df[
        (df[column] < lower)
        | (df[column] > upper)
    ]

    return outliers


# ==========================================
# CORRELATION MATRIX
# ==========================================

def correlation_matrix(df):

    numeric_df = df.select_dtypes(
        include=np.number
    )

    return numeric_df.corr()


# ==========================================
# CHARTS
# ==========================================

def line_chart(df, column):

    fig = px.line(
        df,
        y=column,
        title=f"{column} Trend"
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig


def histogram_chart(df, column):

    fig = px.histogram(
        df,
        x=column,
        nbins=30,
        title=f"{column} Distribution"
    )

    return fig


def box_plot(df, column):

    fig = px.box(
        df,
        y=column,
        title=f"{column} Outlier Analysis"
    )

    return fig


def scatter_plot(df, x_col, y_col):

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{x_col} vs {y_col}"
    )

    return fig


# ==========================================
# HEATMAP
# ==========================================

def correlation_heatmap(df):

    corr = correlation_matrix(df)

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlation Heatmap"
    )

    return fig


# ==========================================
# COUNTRY ANALYTICS
# ==========================================

def country_summary(df, country_col):

    summary = (
        df.groupby(country_col)
        .size()
        .reset_index(name="Count")
        .sort_values(
            by="Count",
            ascending=False
        )
    )

    return summary


# ==========================================
# WEATHER INSIGHTS
# ==========================================

def generate_insights(df):

    insights = []

    numeric_cols = get_numeric_columns(df)

    if len(numeric_cols) == 0:
        return ["No numeric columns found"]

    for col in numeric_cols:

        insights.append(
            f"{col} Average = {round(df[col].mean(),2)}"
        )

        insights.append(
            f"{col} Maximum = {round(df[col].max(),2)}"
        )

        insights.append(
            f"{col} Minimum = {round(df[col].min(),2)}"
        )

    return insights


# ==========================================
# DATA QUALITY SCORE
# ==========================================

def data_quality_score(df):

    total_cells = np.product(df.shape)

    missing = df.isnull().sum().sum()

    score = (
        (total_cells - missing)
        / total_cells
    ) * 100

    return round(score, 2)


# ==========================================
# DOWNLOAD DATA
# ==========================================

def convert_df_to_csv(df):

    return df.to_csv(
        index=False
    ).encode("utf-8")


# ==========================================
# TOP N ANALYSIS
# ==========================================

def top_n_values(df, column, n=10):

    return (
        df[column]
        .value_counts()
        .head(n)
        .reset_index()
    )


# ==========================================
# DATE FEATURES
# ==========================================

def add_date_features(df, date_col):

    df[date_col] = pd.to_datetime(
        df[date_col]
    )

    df["Year"] = df[date_col].dt.year
    df["Month"] = df[date_col].dt.month
    df["Day"] = df[date_col].dt.day

    return df


# ==========================================
# EXTREME WEATHER DETECTION
# ==========================================

def get_extreme_weather(df, column):

    highest = df.nlargest(10, column)

    lowest = df.nsmallest(10, column)

    return highest, lowest
