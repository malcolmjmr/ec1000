import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def problem1_means(income_means_df):
    colors = sns.color_palette("Set2", len(income_means_df.columns))

    years = income_means_df.index.values
    plt.figure(figsize=(20,10))
    # Plot means for each planet 
    for planet, color in zip(income_means_df.columns, colors):
        line = '--' if planet == 'Solar System' else '-'
        means = income_means_df[planet].values

        plt.plot(years, means, line, color=color, label=planet)

    plt.title('Income Means by Year', fontsize=36, y=1.05)
    plt.legend(title='Planets',bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=16)
    plt.xlabel('Year', fontsize=16)
    plt.ylabel('Income Mean', fontsize=16)
    plt.show()

def problem2_lorenzos(gini_coefs_df, income_shares):
    plt.close('all')

    years = gini_coefs_df.index.values
    planets = gini_coefs_df.columns.values
    planet_year_pairs = [(planet, year) for planet in planets for year in years]

    f, axes = plt.subplots(len(planets), len(years), sharex=True, sharey=True, figsize=(20,50))

    for i, ((planet, year), ax) in enumerate(zip(planet_year_pairs,axes.ravel())):

        income_bins = income_shares[planet][year]
        pop_pct = diag_line = sorted(income_bins.keys())
        income_pct = sorted([y for area, y in income_bins.values()])
        ax.fill_between(pop_pct, 0, income_pct)
        ax.plot(pop_pct, diag_line, '--', color='red', label='Equality Line')
        ax.text(0.5,0.25,round(gini_coefs_df.ix[year,planet],4), fontweight='bold', fontsize=36)
        ax.set_ylim(0,1)
        legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')

        if year == years[0]:
            ax.set_ylabel(planet, fontsize='36')

        if planet == planets[0]:
            ax.set_title(year, fontsize='36')

    f.suptitle('Lorenzo Curves for Planets by Year', y=0.93, fontsize=48, fontweight='bold')
    plt.show()
    
def problem2_ginis(gini_coefs_df):
    colors = sns.color_palette("husl", len(gini_coefs_df.columns))

    years = gini_coefs_df.index.values

    plt.figure(figsize=(20,10))

    # Plot gini coefficients
    for planet, color in zip(gini_coefs_df.columns, colors):
        line = '--' if planet == 'Solar System' else '-'
        coefs = gini_coefs_df[planet].values

        plt.plot(years, coefs, line, color=color, label=planet)

    plt.title('Gini Coefficients by Year', y=1.05, fontsize=36, fontweight='bold')
    plt.legend(title='Planets',bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=18)
    plt.xlabel('Year', fontsize=16)
    plt.ylabel('Gini Coefficient', fontsize=16)
    plt.show()
    
def lorenzo(gini_coefs_df, income_shares):
    f, axes = plt.subplots(1, len(gini_coefs_df.index), sharey=True, figsize=(20,5))

    for year, ax in zip(gini_coefs_df.index,axes.ravel()):

        income_bins = income_shares[year]
        pop_pct = diag_line = sorted(income_bins.keys())
        income_pct = sorted([y for area, y in income_bins.values()])
        ax.fill_between(pop_pct, 0, income_pct)
        ax.plot(pop_pct, diag_line, '--', color='red', label='Equality Line')
        ax.text(0.6,0.20,round(gini_coefs_df.ix[year],4), fontweight='bold', fontsize=36)
        ax.set_ylim(0,1)
        legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')
        ax.set_xlabel(year, fontsize=24, fontweight='bold')

    f.suptitle('Lorenzo Curves for Solar System by Year', y=1.05, fontsize=48, fontweight='bold')
    plt.show()