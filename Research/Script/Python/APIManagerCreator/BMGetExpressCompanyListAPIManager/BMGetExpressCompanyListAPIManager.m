//
//  BMGetExpressCompanyListAPIManager.m
//  BMWash
//
//  Created by BobWong on 16/12/16.
//  Copyright © 2016年 月亮小屋（中国）有限公司. All rights reserved.
//

#import "BMGetExpressCompanyListAPIManager.h"

@implementation BMGetExpressCompanyListAPIManager

- (NSString *)interfaceUrl
{
    return INTERFACE_GET_EXPRESS_COMPANY_LIST;
}

- (BOOL)useToken
{
    return YES;
}

@end
