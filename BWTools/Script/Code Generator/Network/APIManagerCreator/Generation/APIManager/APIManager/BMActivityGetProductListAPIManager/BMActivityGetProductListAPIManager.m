//
//  BMActivityGetProductListAPIManager.m
//  BlueMoonHouse
//
//  Created by BobWong on 17/05/24.
//  Copyright © 2017年 月亮小屋（中国）有限公司. All rights reserved.

#import "BMActivityGetProductListAPIManager.h"
#import "BMUserCenter.h"
#import "BMConstantMacroMessage.h"

@interface BMActivityGetProductListAPIManager () <BMAPIManager, BMAPIManagerInterceptor, BMAPIManagerValidator>

@property (nonatomic, copy, readwrite) NSString *errorMessage;

@end

@implementation BMActivityGetProductListAPIManager

#pragma mark - 生命周期

- (instancetype)init
{
    self = [super init];
    if (self) {
        self.validator = self;
        self.interceptor = self;
    }
    return self;
}

#pragma mark - BMAPIManager manager

- (NSString *)methodName
{
    return @"BMActivityGetProductListAPIManager";
}

- (NSString *)serviceIdentifier
{
    return kBMServiceIdActivityGetProductList;
}

- (BMAPIManagerRequestType)requestType
{
    return BMAPIManagerRequestTypeJSONPost;
}

- (BOOL)shouldCache
{
    return NO;
}

#pragma mark - BMAPIManagerValidator 验证器

- (BOOL)manager:(BMBaseAPIManager *)manager isCorrectWithCallBackData:(NSDictionary *)data
{
    if (!isAPICallingSuccess(data)) {
        self.errorMessage = getAPICallingResponseMsg(data);
        return NO;
    }
    return YES;
}

- (BOOL)manager:(BMBaseAPIManager *)manager isCorrectWithParamsData:(NSDictionary *)data
{
    return YES;
}

#pragma mark - BMAPIManagerInterceptor 拦截器
//是否允许调用api
- (BOOL)manager:(BMBaseAPIManager *)manager shouldCallAPIWithParams:(NSDictionary *)params
{
    if (![BMUserCenter sharedInstance].isLogined) {
        self.errorMessage = BMMessageNotAllowCallingAPI;
        [[NSNotificationCenter defaultCenter] postNotificationName:BMNOTIFICATION_REQUEST_LOGIN object:@{kBMManager: manager,kBMLoginReason:@(LoginReasonUserLoginAndPrompt)}];
        return NO;
    }
    if (![BMUserCenter sharedInstance].istokenValid) {
        [[NSNotificationCenter defaultCenter] postNotificationName:BMNOTIFICATION_REQUEST_LOGIN object:@{kBMManager: manager,kBMLoginReason:@(LoginReasonTokenInvalidAndPrompt)}];
        return NO;
    }
    return YES;
}

#pragma mark - 重写父类格式化参数方法

- (NSDictionary *)reformParams:(NSDictionary *)params
{
    NSMutableDictionary *mutableParams = params?[[super reformParams:params] mutableCopy]:[[NSMutableDictionary alloc] init];
    NSString *token = [BMUserCenter sharedInstance].token;
    [mutableParams setObject:token forKey:kBMToken];
    return mutableParams;
}

@end
