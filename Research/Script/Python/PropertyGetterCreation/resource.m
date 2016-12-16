@property (nonatomic, strong) UIScrollView *scrollView;  ///< Scroll View

@property (nonatomic, strong) UIButton *btnSelectAddress;  ///< 选择地址Button
@property (nonatomic, strong) UIImageView *ivLocationIcon;  ///< 定位Icon ImageView
@property (nonatomic, strong) UILabel *lbLocation;  ///< 地址
@property (nonatomic, strong) UIImageView *ivArrow;  ///< 箭头

@property (nonatomic, strong) UIView *viewMiddle;  ///< 中间View
@property (nonatomic, strong) UILabel *lbGetClothesWayDesc;  ///< 收衣方式描述
@property (nonatomic, strong) UIButton *btnGetClothesVisit;  ///< 上门收衣
@property (nonatomic, strong) UIButton *btnGetClothesExpress;  ///< 快递
@property (nonatomic, strong) UIView *viewGetClothesMsg;  ///< 收衣方式信息视图，根据所选收衣方式，显示不同内容
@property (nonatomic, strong) UILabel *lbFeeDesc;  ///< 上门收衣费描述
@property (nonatomic, strong) UILabel *lbFee;  ///< 上门收衣
@property (nonatomic, strong) UILabel *lbSendTip0;  ///< 寄送提示
@property (nonatomic, strong) UILabel *lbSendTargetPerson;  ///< 寄送目标人员的姓名和联系方式
@property (nonatomic, strong) UILabel *lbSendTargetLocation;  ///< 寄送目标地址

@property (nonatomic, strong) UILabel *lbRemarkDesc;  ///< 备注描述
@property (nonatomic, strong) UILabel *lbRemark;  ///< 备注

@property (nonatomic, strong) UIButton *btnConfirm;  ///< 确认预约
