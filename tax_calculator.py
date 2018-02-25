

######################################################################################################################
#
#   IRS Tax Brackets:
#   https://www.irs.com/articles/2017-federal-tax-rates-personal-exemptions-and-standard-deductions
#
#   Calculator:
#   https://www.taxact.com/tools/tax-bracket-calculator.asp
#
#   Usage:
#       tax_calculator.py 200000 married_joint 18000
#       tax_calculator.py 100000 married_seperately 18000
#
######################################################################################################################


import sys


def z_tax_estimate(gross_income, filing_status, retirement_contribution):
    
    # Money put towards 401k retirement
    retirement_contribution = retirement_contribution
    
    # Standard Tax Rates    
    percent_state_tax_rate      = 0.05499   # https://www.ncdor.gov/tax-rate-tax-year-2017
    percent_medicare_rate       = 0.0145    # https://www.irs.gov/taxtopics/tc751
    percent_social_security     = 0.0620    # https://www.irs.gov/taxtopics/tc751
    std_deduction_married_joint = 12700     # https://www.irs.com/articles/2017-federal-tax-rates-personal-exemptions-and-standard-deductions 
    std_deduction_married_sep   = 6350      # https://www.irs.com/articles/2017-federal-tax-rates-personal-exemptions-and-standard-deductions
    
    # Pre-tax Calculations:
    socialsecurity = (gross_income * percent_social_security) if gross_income < 127200 else (127200 * percent_social_security)
    socialsecurity = socialsecurity*2 if filing_status=='married_joint' else socialsecurity
    medicare       = gross_income * percent_medicare_rate
    
    # Taxable Income
    standard_deduction = std_deduction_married_joint if filing_status=='married_joint' else std_deduction_married_sep
    taxable_income     = gross_income - retirement_contribution - standard_deduction
    
    if filing_status == 'married_joint':
        if 75901 <= taxable_income <= 153100:
            # 25% Tax Bracket
            tax_bracket          = '25%'
            federal_tax_rate     = 0.25
            federal_tax_initial  = 10452.50
            federal_tax_over_amt = 75900
        elif 153101 <= taxable_income <= 233350:
            # 28% Tax Bracket
            tax_bracket          = '28%'
            federal_tax_rate     = 0.28
            federal_tax_initial  = 29752.50
            federal_tax_over_amt = 153100
        elif 233351 <= taxable_income <= 416700:
            # 33% Tax Bracket
            tax_bracket          = '33%'
            federal_tax_rate     = 0.33
            federal_tax_initial  = 52222.50
            federal_tax_over_amt = 233350
        elif 416701 <= taxable_income <= 470700:
            # 35% Tax Bracket
            tax_bracket          = '35%'
            federal_tax_rate     = 0.35
            federal_tax_initial  = 112728
            federal_tax_over_amt = 416700
        elif taxable_income >= 470701:
            # 35% Tax Bracket
            tax_bracket          = '39.6%'
            federal_tax_rate     = 0.35
            federal_tax_initial  = 131628
            federal_tax_over_amt = 470700
        else:
            tax_bracket = 'other'
            tax_bracket          = ''
            federal_tax_rate     = 0
            federal_tax_initial  = 0
            federal_tax_over_amt = 0
    elif filing_status == 'married_seperately':
        if 37951 <= taxable_income <= 76550:
            # 25% Tax Bracket
            tax_bracket          = '25%'
            federal_tax_rate     = 0.25
            federal_tax_initial  = 5226.25
            federal_tax_over_amt = 37950
        elif 76551 <= taxable_income <= 116675:
            # 28% Tax Bracket
            tax_bracket          = '28%'
            federal_tax_rate     = 0.28
            federal_tax_initial  = 14876.25
            federal_tax_over_amt = 76550
        elif 116676 <= taxable_income <= 208350:
            # 33% Tax Bracket
            tax_bracket          = '33%'
            federal_tax_rate     = 0.33
            federal_tax_initial  = 26111.25
            federal_tax_over_amt = 116675
        elif 208351 <= taxable_income <= 235350:
            # 35% Tax Bracket
            tax_bracket          = '35%'
            federal_tax_rate     = 0.35
            federal_tax_initial  = 56364
            federal_tax_over_amt = 208350
        elif taxable_income >= 235351:
            # 39.6% Tax Bracket
            tax_bracket          = '39.6%'
            federal_tax_rate     = 0.396
            federal_tax_initial  = 65814
            federal_tax_over_amt = 235350
        else:
            tax_bracket = 'other'
            tax_bracket          = ''
            federal_tax_rate     = 0
            federal_tax_initial  = 0
            federal_tax_over_amt = 0
    
    # Federal and State Tax Witholdings:    
    fed_taxes    = federal_tax_initial + ((taxable_income - federal_tax_over_amt) * federal_tax_rate)
    state_taxes  = taxable_income * percent_state_tax_rate
    
    takehome_pay = taxable_income - fed_taxes - state_taxes - socialsecurity - medicare
    total_taxes  = fed_taxes + state_taxes + socialsecurity + medicare
    
    return [gross_income, taxable_income, takehome_pay, tax_bracket, total_taxes, fed_taxes, (fed_taxes/float(taxable_income)), state_taxes, retirement_contribution, socialsecurity, medicare]


if __name__ == "__main__":
    
    try:
        gross_income  = int(sys.argv[1])
        filing_status = sys.argv[2]
        retirement_contribution = int(sys.argv[3])  
    except:
        print('\n\n[ USAGE ] tax_calculator.py <gross_income> <filing_status=married_joint|married_seperately> <retirement_contribution=18000>\n\n')
        sys.exit()
    
    results = z_tax_estimate(gross_income, filing_status, retirement_contribution)
    
    print('\n\n')
    print('Gross Income:        '+str(results[0]))
    print('Taxable Income:      '+str(results[1]))
    print('Takehome Pay:        '+str(results[2]))
    print('Tax Bracket:         '+str(results[3]))
    print('Total Taxes:         '+str(results[4]))
    print('Federal Tax:         '+str(results[5]))
    print('Federal Tax (%):     '+str(results[6]))
    print('State Tax:           '+str(results[7]))
    print('Retirement Contrib:  '+str(results[8]))
    print('Social Security:     '+str(results[9]))
    print('Medicare:            '+str(results[10]))
    print('\n\n')


#ZEND