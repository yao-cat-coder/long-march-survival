import streamlit as st

st.set_page_config(page_title="长征·雪山求生", page_icon="🏔️")
st.title("🏔️ 长征·翻越夹金山")
st.write("""夹金山是红军穿越的第一座雪山，它既是地理上的天险，更是战略上的关键隘口。
翻越夹金山当地民谣唱道：夹金山，夹金山，鸟儿飞不过，人也不可攀。要想越过夹金山，除非神仙到人间。
蒋介石重兵围追堵截，封锁川西要道，这座看似不可能翻阅的神山成了红军唯一可能出其不意、快速北上的生路。
作为先遣队的红四团进入了雪山，而你作为这只先遣队的领导者，任务是带领部队活下去！！！""")

st.markdown("""
<style>
.history-box {
    background-color: rgba(200, 180, 150, 0.1);
    border-left: 5px solid #d9534f;
    padding: 15px;
    margin: 10px 0;
    border-radius: 5px;
    color: #e0e0e0 !important;
}
.danger-box {
    background-color: rgba(255, 0, 0, 0.1); 
    border: 2px solid #ff4b4b; 
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
}
.success-card {
    background-color: rgba(0, 255, 0, 0.1); 
    border-left: 8px solid #00ff00; 
    padding: 10px 20px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.5); 
}
</style>
""", unsafe_allow_html=True)

if "stage" not in st.session_state:
    st.session_state.stage = 1

st.divider()

if st.session_state.stage == 1:
    st.subheader("第一关：御寒衣物的筹集")
    st.write("""
    国民党长期的反动宣传。受“红军要吃人肝”等谣言恐吓，当地藏族同胞纷纷躲进深山，村落一度人去楼空。
    
    你该如何筹集物资？
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("带武器冲进仅存的村落，强行征收衣服和粮食"):
            st.error("""💀 **全军覆没！**
            因为你的举动更加坐实了国民党的宣传，没有村落剩余，因为抢到的衣物和粮食太少了，他们倒下后就再也没有站起来，很多人冻伤饿死。
            
            最后你也撑不住，冻死了。""")
            st.markdown("""
            <div class="danger-box">
                <b>📜 历史档案：</b> 军需处长：负责全团御寒物资调配，手里有棉衣，“但一件都没有留给自己”，穿着单衣冻死在夹金山雪地里。<br>
                红一方面军过夹金山时“大多穿着草鞋，身上只有单衣”，有战士走不动停下，“一摸，人已经冻住了”。
            </div>
            """, unsafe_allow_html=True)
            if st.button("重新选择"):
                st.session_state.stage = 1
                st.rerun()
                
    with col2:
        if st.button("严格执行民族政策，不拿群众一物，按价购买"):
            st.success(""" **出发！**
            严明的纪律最终感化了群众，使他们从躲藏转为拥护。
            
            筹集到羊皮、棉衣、白酒、辣椒等，虽受当地贫瘠条件限制无法满足全部需求，但根本上维护了红军的信誉。""")
            st.markdown("""
            <div class="success-card">
            <b>📜 历史档案：</b> 邹衍所在部队在夹金山下得知先头部队因准备不足有人冻死后，领导要求“立足现有条件”准备。战士们把两件单衣缝在一起絮上羊毛，<br>
            蔡畅亲自教战士絮套子、做示范，部队最终穿着自制的御寒衣翻过了夹金山。
            </div>
            """, unsafe_allow_html=True)
            if st.button("带着物资继续上山"):
                st.session_state.stage = 2
                st.rerun()

elif st.session_state.stage == 2:
    st.subheader("第二关：冰雪路面无防滑装备")
    st.write("""
    雪下藏着暗冰，路面溜滑。每抬一步，都很吃力。稍有不慎，就会摔下去。
    
    而没有防滑装备，就等于把每一次落脚都变成一次赌博。
    
    但有效的防滑装备，从源头上就“没有”。而你该怎么解决这个问题？
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("不管防滑，直接硬闯，让战士们注意一点"):
            st.error("""💀 **全军覆没！**
            尖兵站不稳、凿不出踏脚孔，后续无足迹可循；
            
            草鞋无抓地力，踩偏即滑坠，结队缺失还会导致连锁坠崖；
            
            行军速度崩溃，停留更久，冻伤、冻亡成倍上升；
            
            足迹被新雪冰雹抹掉，后队迷路掉队，建制难以维持；
            
            先遣队自身难通过，更无法为全军开路，北上会师进程可能被阻断。""")
            st.markdown("""
            <div class="history-box">
                <b>📜 历史档案：</b> 吴先恩部翻党岭山遇鸡蛋大冰雹，有的战士瞬间跌入深谷，有的战士滑入雪坑甚至被冻住，永远没有再站起来。
            </div>
            """, unsafe_allow_html=True)
            if st.button("重新选择"):
                st.session_state.stage = 2
                st.rerun()
                
    with col2:
        if st.button("向猎户学习，自制“脚马子”并结队前行"):
            st.success("""**继续前行**
            少数尖兵靠脚马子或钉鞋勉强开路，多数人靠布条麻绳、拐棍和结队沿足迹前行，维持了先遣队基本通过。
            
            行军速度慢、冻伤磨伤多，滑坠和连锁坠崖造成严重牺牲。
            
            以巨大代价完成了开路任务。""")
            st.markdown("""
            <div class="success-card">
            <b>📜 历史档案：</b> 高秀英的防滑钉鞋：鞋底嵌一圈圆头铁钉，麻布为面，穿着它翻越雪山，现藏中国国家博物馆。<br>
            红四方面军先遣队穿着从猎户手中换得的“脚马子”走在前面攀冰开路，后续部队沿踏出的脚印上行。防滑器“大大提高了前进速度，并减少了因失足滑倒跌入雪山深渊的危险”。
            </div>
            """, unsafe_allow_html=True)
            if st.button("继续向更高处攀登"):
                st.session_state.stage = 3
                st.rerun()

elif st.session_state.stage == 3:
    st.subheader("第三关：坐下的诱惑")
    st.write("""
    在极度寒冷与疲惫下，许多战士控制不住的想要静坐休息，你看着他们疲惫的神情和满是冻伤的双手。
    
    有战士问你，能不能坐下来休息一会？
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("静坐休息"):
            st.error("""💀 **全军覆没！**
            极度寒冷与疲惫会麻痹神经，让人产生虚假的温暖舒适感，停下坐下休息成了致命的诱惑。
            
            那些坐下的战士，体温在静坐中飞速流失，在原地被冻僵，飞雪很快为他们盖上“被子”。""")
            st.markdown("""
            <div class="danger-box">
                <b>📜 历史档案：</b> 郝毅误将烈士遗体当成石头：老红军郝毅在翻越夹金山时，因极度疲惫想歇息，朦胧中看见前面有一块大石头，便把包袱放上去想坐下。谁知刚一坐下，大石头就歪倒了——原来那是前面部队牺牲的战友，身子已经冻僵了。
            </div>
            """, unsafe_allow_html=True)
            if st.button("重新选择"):
                st.session_state.stage = 3
                st.rerun()
                
    with col2:
        if st.button("带头高呼“千万不要坐下”"):
            st.success("""**继续前行**
            你选择了互相搀扶、强帮弱、大助小。在极度缺氧和严寒中，大家用绑腿结成绳索，用身躯相互取暖。
            
            虽然许多人冻坏了脚趾，但你们成功突破了生理极限，全连无一人掉队，建制完整保全！
            
            这一刻，你们用生命书写了什么是真正的战友情。""")
            st.markdown("""
            <div class="success-card">
                <b>📜 历史档案：</b> 翻越夹金山时，双腿负过重伤的陈赓身先士卒，困难时带头高呼口号：“千万不要坐下！坚持就是胜利！”干部团在他的鼓励下成功征服了雪山。因积累了经验，后续翻越海拔5000多米的打鼓山时，大家在顶峰甚至还有兴致吃雪拌糖精当“冰激凌”。<br><br>
                红四团通过干部带头、互相搀扶翻越夹金山，实现了“无一人掉队”。袁学凯部在冰雹与狂风中互相拉扯前行，翻山后清点，人员与装备“无一损失”。
            </div>
            """, unsafe_allow_html=True)
            if st.button("继续向更高处攀登"):
                st.session_state.stage = 4
                st.rerun()

elif st.session_state.stage == 4:
    st.subheader("第四关：雪盲与死神的暴风雪")
    st.write("""
    接近山顶时，天色骤变。狂风卷着鸡蛋大的冰雹劈头盖脸砸下，湿透的单衣瞬间结成了冰壳。
    
    更糟的是，强烈的雪光让大量战士患上雪盲，泪流不止，失去了方向感。有人提议，用绑腿把大家串连在一起，互相拉扯着冲顶。
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("把所有人用绑腿绳串起来，顶着暴风雪强行冲顶"):
            st.error("""💀 **全军覆没！**
            你们以为绳子是救命稻草，却成了催命符。狂风刮来，一名失明的战士脚滑坠崖，结绳导致后面的战士来不及松手，一个接一个被拽下山谷。
            
            留在原地休息的战士，在冰雹中被活活砸死。队伍建制彻底溃散。""")
            st.markdown("""
            <div class="danger-box">
                <b>📜 历史档案：</b> 有战士用腰带结绳牵着雪盲战友前行，狂风刮来一人滚下山，其他人来不及松手，一个接一个被拽下去，四五个同志就这样牺牲了。<br><br>
                红四方面军一位女红军卫生员回忆：一部分人坚持“翻过山再休息”，另一部分人因疲惫不堪决定在山脚下过夜。第二天清晨，战友上山去叫醒他们时，发现留在山上的60多人全部被夜间的冰雹活活砸死。
            </div>
            """, unsafe_allow_html=True)
            if st.button("重新选择"):
                st.session_state.stage = 4
                st.rerun()
                
    with col2:
        if st.button("停止冲锋，用布条蒙眼避风，等待老乡说的天气窗口期"):
            st.success("""**继续前行**
            你没有被恐惧吞噬，下令全员原地围圈抱团，用布条遮住眼睛缓解雪盲。
            
            你们熬过了最猛烈的冰雹，趁着天气短暂放晴的窗口期，采取“强帮弱、大助小”的纪律，成功翻过了主峰！""")
            st.markdown("""
            <div class="success-card">
                <b>📜 历史档案：</b> 行动前，红四团领导层深入当地访问，从年长老乡那里获取了生存情报：必须在上午9时以后、下午3时以前通过，绝不能在早晚风雪最烈时过山。<br><br>
                红四团严格执行了时间纪律。1935年6月12日清晨9时许，部队正式进发，力求在天气相对平缓的窗口期通过。遇到战士滑入雪坑，指挥员迅速组织解下绑腿扭成布绳营救，这种有纪律的互助，是建制得以保全的关键。
            </div>
            """, unsafe_allow_html=True)
            if st.button("走向最终的胜利"):
                st.session_state.stage = 5
                st.rerun()

elif st.session_state.stage == 5:
    st.balloons()
    st.success("🚩 **红旗漫卷西风！** 你们成功翻越了夹金山，率先在达维镇与红四方面军先头部队胜利会师！")
    
    st.markdown("""
    <div class="success-card">
        <b>📜 历史回响：</b> 1935年6月，红四团作为全军先锋，用血肉之躯趟出了这条生命线。这座被当地人称为“鸟儿飞不过”的神山，被这群穿着草鞋、嚼着辣椒的年轻人彻底征服。但先遣队的脚步没有停下，前方还有更致命的茫茫草地等待着你们……
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🏆 游戏通关！先遣队使命达成！")
    st.write("**思政小贴士**：长征不仅是一次军事上的战略转移，更是一次理想信念的伟大远征。红军将士靠着坚定的革命信念、官兵一致的团结精神以及人民群众的拥护，战胜了极寒与缺氧。今天，我们通过代码重温这段历史，是为了在新时代的长征路上，继续传承这份不屈的精神！")
    
    if st.button("重走长征路（重新开始）"):
        st.session_state.stage = 1
        st.rerun()