//
//  BMAppointmentSaveAPIManager.m
//  BMWash
//
//  Created by BobWong on 16/12/17.
//  Copyright © 2016年 月亮小屋（中国）有限公司. All rights reserved.
//

#import "BMAppointmentSaveAPIManager.h"

@implementation BMAppointmentSaveAPIManager

- (NSString *)interfaceUrl
{
    return INTERFACE_APPOINTMENT_SAVE;
}

- (BOOL)useToken
{
    return YES;
}

@end
