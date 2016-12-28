//
//  BMAppointmentGetCollectTypeAPIManager.m
//  BMWash
//
//  Created by BobWong on 16/12/17.
//  Copyright © 2016年 月亮小屋（中国）有限公司. All rights reserved.
//

#import "BMAppointmentGetCollectTypeAPIManager.h"

@implementation BMAppointmentGetCollectTypeAPIManager

- (NSString *)interfaceUrl
{
    return INTERFACE_APPOINTMENT_GET_COLLECT_TYPE;
}

- (BOOL)useToken
{
    return YES;
}

@end
