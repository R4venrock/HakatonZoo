PGDMP                         {            zoo_quiz    14.8 (Homebrew)    15.2 /    1           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            2           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            3           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            4           1262    16499    zoo_quiz    DATABASE     j   CREATE DATABASE zoo_quiz WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE zoo_quiz;
                ksenia    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                ksenia    false            5           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   ksenia    false    4            �            1259    16544    animal_results    TABLE     �   CREATE TABLE public.animal_results (
    id character varying(50) NOT NULL,
    image text NOT NULL,
    result_text text NOT NULL,
    animal_url text
);
 "   DROP TABLE public.animal_results;
       public         heap    ksenia    false    4            �            1259    16543    animal_results_id_seq    SEQUENCE     �   CREATE SEQUENCE public.animal_results_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.animal_results_id_seq;
       public          ksenia    false    219    4            6           0    0    animal_results_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.animal_results_id_seq OWNED BY public.animal_results.id;
          public          ksenia    false    218            �            1259    16506    quiz    TABLE     �  CREATE TABLE public.quiz (
    id integer NOT NULL,
    id_question integer NOT NULL,
    question text NOT NULL,
    id_answer numeric NOT NULL,
    answer text NOT NULL,
    penguin integer NOT NULL,
    owl integer NOT NULL,
    bear integer NOT NULL,
    lori integer,
    irbis integer,
    tiger integer,
    eagle integer,
    bird_sec integer,
    vicuna integer,
    cuscus integer,
    crocodile integer,
    manul integer,
    seal integer,
    otter integer
);
    DROP TABLE public.quiz;
       public         heap    ksenia    false    4            �            1259    16505    quiz_bear_seq    SEQUENCE     �   CREATE SEQUENCE public.quiz_bear_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.quiz_bear_seq;
       public          ksenia    false    215    4            7           0    0    quiz_bear_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.quiz_bear_seq OWNED BY public.quiz.bear;
          public          ksenia    false    214            �            1259    16502    quiz_id_answer_seq    SEQUENCE     �   CREATE SEQUENCE public.quiz_id_answer_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.quiz_id_answer_seq;
       public          ksenia    false    215    4            8           0    0    quiz_id_answer_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.quiz_id_answer_seq OWNED BY public.quiz.id_answer;
          public          ksenia    false    211            �            1259    16501    quiz_id_question_seq    SEQUENCE     �   CREATE SEQUENCE public.quiz_id_question_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.quiz_id_question_seq;
       public          ksenia    false    4    215            9           0    0    quiz_id_question_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.quiz_id_question_seq OWNED BY public.quiz.id_question;
          public          ksenia    false    210            �            1259    16500    quiz_id_seq    SEQUENCE     �   CREATE SEQUENCE public.quiz_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.quiz_id_seq;
       public          ksenia    false    4    215            :           0    0    quiz_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE public.quiz_id_seq OWNED BY public.quiz.id;
          public          ksenia    false    209            �            1259    16504    quiz_owl_seq    SEQUENCE     �   CREATE SEQUENCE public.quiz_owl_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.quiz_owl_seq;
       public          ksenia    false    215    4            ;           0    0    quiz_owl_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.quiz_owl_seq OWNED BY public.quiz.owl;
          public          ksenia    false    213            �            1259    16503    quiz_penguin_seq    SEQUENCE     �   CREATE SEQUENCE public.quiz_penguin_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.quiz_penguin_seq;
       public          ksenia    false    4    215            <           0    0    quiz_penguin_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.quiz_penguin_seq OWNED BY public.quiz.penguin;
          public          ksenia    false    212            �            1259    16535    reviews    TABLE     �   CREATE TABLE public.reviews (
    id integer NOT NULL,
    id_user integer NOT NULL,
    username character varying(50),
    review text NOT NULL
);
    DROP TABLE public.reviews;
       public         heap    ksenia    false    4            �            1259    16534    reviews_id_seq    SEQUENCE     �   CREATE SEQUENCE public.reviews_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.reviews_id_seq;
       public          ksenia    false    4    217            =           0    0    reviews_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.reviews_id_seq OWNED BY public.reviews.id;
          public          ksenia    false    216            �           2604    16552    animal_results id    DEFAULT     v   ALTER TABLE ONLY public.animal_results ALTER COLUMN id SET DEFAULT nextval('public.animal_results_id_seq'::regclass);
 @   ALTER TABLE public.animal_results ALTER COLUMN id DROP DEFAULT;
       public          ksenia    false    219    218    219            �           2604    16509    quiz id    DEFAULT     b   ALTER TABLE ONLY public.quiz ALTER COLUMN id SET DEFAULT nextval('public.quiz_id_seq'::regclass);
 6   ALTER TABLE public.quiz ALTER COLUMN id DROP DEFAULT;
       public          ksenia    false    215    209    215            �           2604    16510    quiz id_question    DEFAULT     t   ALTER TABLE ONLY public.quiz ALTER COLUMN id_question SET DEFAULT nextval('public.quiz_id_question_seq'::regclass);
 ?   ALTER TABLE public.quiz ALTER COLUMN id_question DROP DEFAULT;
       public          ksenia    false    210    215    215            �           2604    16525    quiz id_answer    DEFAULT     p   ALTER TABLE ONLY public.quiz ALTER COLUMN id_answer SET DEFAULT nextval('public.quiz_id_answer_seq'::regclass);
 =   ALTER TABLE public.quiz ALTER COLUMN id_answer DROP DEFAULT;
       public          ksenia    false    215    211    215            �           2604    16512    quiz penguin    DEFAULT     l   ALTER TABLE ONLY public.quiz ALTER COLUMN penguin SET DEFAULT nextval('public.quiz_penguin_seq'::regclass);
 ;   ALTER TABLE public.quiz ALTER COLUMN penguin DROP DEFAULT;
       public          ksenia    false    215    212    215            �           2604    16513    quiz owl    DEFAULT     d   ALTER TABLE ONLY public.quiz ALTER COLUMN owl SET DEFAULT nextval('public.quiz_owl_seq'::regclass);
 7   ALTER TABLE public.quiz ALTER COLUMN owl DROP DEFAULT;
       public          ksenia    false    213    215    215            �           2604    16514 	   quiz bear    DEFAULT     f   ALTER TABLE ONLY public.quiz ALTER COLUMN bear SET DEFAULT nextval('public.quiz_bear_seq'::regclass);
 8   ALTER TABLE public.quiz ALTER COLUMN bear DROP DEFAULT;
       public          ksenia    false    214    215    215            �           2604    16538 
   reviews id    DEFAULT     h   ALTER TABLE ONLY public.reviews ALTER COLUMN id SET DEFAULT nextval('public.reviews_id_seq'::regclass);
 9   ALTER TABLE public.reviews ALTER COLUMN id DROP DEFAULT;
       public          ksenia    false    217    216    217            .          0    16544    animal_results 
   TABLE DATA           L   COPY public.animal_results (id, image, result_text, animal_url) FROM stdin;
    public          ksenia    false    219   �1       *          0    16506    quiz 
   TABLE DATA           �   COPY public.quiz (id, id_question, question, id_answer, answer, penguin, owl, bear, lori, irbis, tiger, eagle, bird_sec, vicuna, cuscus, crocodile, manul, seal, otter) FROM stdin;
    public          ksenia    false    215   �>       ,          0    16535    reviews 
   TABLE DATA           @   COPY public.reviews (id, id_user, username, review) FROM stdin;
    public          ksenia    false    217   ZG       >           0    0    animal_results_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.animal_results_id_seq', 1, false);
          public          ksenia    false    218            ?           0    0    quiz_bear_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.quiz_bear_seq', 51, true);
          public          ksenia    false    214            @           0    0    quiz_id_answer_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.quiz_id_answer_seq', 1, false);
          public          ksenia    false    211            A           0    0    quiz_id_question_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.quiz_id_question_seq', 1, false);
          public          ksenia    false    210            B           0    0    quiz_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.quiz_id_seq', 1, false);
          public          ksenia    false    209            C           0    0    quiz_owl_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.quiz_owl_seq', 51, true);
          public          ksenia    false    213            D           0    0    quiz_penguin_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.quiz_penguin_seq', 51, true);
          public          ksenia    false    212            E           0    0    reviews_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.reviews_id_seq', 1, false);
          public          ksenia    false    216            �           2606    16554 "   animal_results animal_results_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.animal_results
    ADD CONSTRAINT animal_results_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.animal_results DROP CONSTRAINT animal_results_pkey;
       public            ksenia    false    219            �           2606    16518    quiz quiz_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.quiz
    ADD CONSTRAINT quiz_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.quiz DROP CONSTRAINT quiz_pkey;
       public            ksenia    false    215            �           2606    16542    reviews reviews_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.reviews DROP CONSTRAINT reviews_pkey;
       public            ksenia    false    217            .   �  x��Y[o��~�~�EH")QXiѤI�M�b�)P�8�Hf-�ZR��}�ݭ��4�E�t� m�>ɲe�����'�23�����,[&�e�o�Z.�Y�t�Ừ��C��z�����v��9�g5|{Cuu��i�߉^F}%ލ��h��h��フׯ��\�~�'�n����U�i4T�xh.L�Q�4>����B�.���>���hࣳ舮L��Cv�q4R����O�D��E�x?:W�'0zwp?y%��$����;��;���x/��_�#�����ܝB{?�-pѽ�G��%L6J�ѿ}xz�9���Qq����Q4\��K�	7�W�ǆ�4n��=����zϢ���3���h�pe�9�+x4sw��,�te �G�5���7�{��p|��Y�k�F�n�{ẽ�깪�z�\�u6]G}/l�,t�<�n�4�z5�o5nf�jYײ�t�+�+0d�S� 9L�mw	������DS��`D����h�y�-0ʇ��4t��]�f�i��Fp���6~�{�8�E_�{�
m�6�G瑽i���#���q� R~��͞�M߷�}��Y�a=���l�����o�b��为V-��s��i��jũ�5W����(�I!����s8�- !G�R���>8p�s
�d�!�aw9�1��]i�9K��~� �C���$p)ZW� �;xWY���p���q��B+_rw��0�7�0�)��:����.)�G�[`h�C,:����Ԅ3_+�J/���)���[� 95��G�o/g� \�}%�z�M&��m���m����W�Z8�i���̀/�1Å�,�J�e%f�Z�.���`����#A��I�
�u����|�F�,��|=I�M6�#�Q2 .�'��� ��1�8#�)��<G��wa0�hw�\I��>�U�D��$It�����|���U�m��k�{��4Xk�Ռ��Z�ڷ�B�T�O�X*����f�f�R4�Q��P�Uq�4���(^��I��Q��L<r"ҝHL�q	�	cnt~SD�p�@XhF�B�K�M��#=ȣZ�yO����L>����q�bIF�R
L���ٜ�a�cb�x��3�e�C�I�`$/�2f�����7��ߘ�o��uB�^w#p;,Xv�����n�%���~;��ZZ%���-?zW��9 v���]��^*�U���꺆�lm����Z{���9m)0�=8�����P���G�K���G\QK�
�<�	�*ę���Hi�ާ+�lI��NdZ��W�V*�f�1�$�? ~�<=E��'0`H��'l���'~'���˄�r�[�,h�g۽zu���z��T�2v7���7�-3W.廡��G��5�u��o>.��{�����k�P,~����C�ۍ��`ا����'��/�����B�{���EC���^�w�,�	�z�k�����nՊ��U.�Qv�r�R2ʎs�^X<\���{�� h�?�m�L'�}n>����G���{��|����ڿ���j�^�N��vﲆ�m�A����y��%�fL�tO�=��~K�	N�P�8#�hN��P@�>� ���Fb�#�z9	����F�r)��ڀ��X��Eq�� f8�cI���5����c���z<#�Hk�^���q�FF�JNPryFG���v!�� �W 8��)��Iwn��n�^g��ކ�	j��v���6�!�,�X�؁o���0q�5�F��`�B���d��L��*L����\�;��`n��:n�k{��W״%ŏ�O�� ��˄b
 ����"�p��?RxO��A�
��z��b�	בct3QR�2�(��?��'��ХYye{�pL�.��C\d�F#$y�yB)H� ���IՓ�|�!OcT�$� ��Ԉ�9@қ���$o�2|L{�<x%�K�*��GX`QBNv�r�A��� ������� ��k�ɰ�	]v��P��8v��JU׬T�b���Z�蠀l�P����W; .�;�-.�_f���L��ʋ���9�;�n�Mg$&)77��Ic�X��(�p���Hʍ�YNCx��vt1�p�SZ~"�4U����lh��祈�M` �gO�.3���KPpI� �_�!F��dUC{9̶���)�6�f�[~���n��0M?7|����Y���鸷�G�U[jHaHag�/��-��9/9��)�`��G�.�q&d����WcuGX�/4'م�V�$�PW�ZJ��5����|9<�I����)��R�+�\��x���<S��S_�<�g�<���s�!�|� I��������=�����뒆��{;e��1_
[3��.<�g�?�dv��^��f$�j�͞\����&ku笵���o���e�UJ5��
��ˆQ��%����S�jU�ZJ}� �l8�|�չ�Ԣ�$����3z.4��;���5�'Ic��)u����,e�"�B�pʿ"���.=Ig�Cv֒�+o>�d���i� ����çT(��K΂`E��R|������W|+���a`d�n���Z�a ���ØYu�l�S+U*e�\� �iz�.,��K*���N��Rt��� ^r��"�`�=H
��lBx��Nx�@�;�ˉ}��C�l���.f�!��Td!")ٗ=�{Z��d>�-[�"�ġ9�TrD$=�X�p*�!��ǻE}��^+U��v�A�J��]^�4����Ϛu�*AC��k ��zAӾ,k��:dP�_�#"QЦ
*�dn�)jP�3˨��i��jͱ���ۺ�^Gc"HQ}Qg94��L�E��I2,�x3EQU��2�t��(yEp�l���j��*�+�TQ�-�\�U��.eҴ�=��b�Q/�O�����G(4�;$k�K�:���g����LD�)��-����SVӢhu�Q�7��v ;���F���������x��i�\�H٩�m˴�k�&3��Q�:��/���x!��7�˕��߹��B�ʒ_�D��+?׮_�L.�޽�R����"Ή4ī;��0%��o��FK��g_���̓�_��c-��;�z�C�*�t@���Iq?����5c&�"{c)�C�l(�G�7M_��1�^&zv�=�,G$��VJ��h^ĉ�k<.&E�'�]Et1���"��.88n�
�j���]�}�~����m�s��9�\��K6�H�����kv�v��妬nf���d2?�Z�       *   �  x��Y�rG]_1�Q $��x��6�"���RJ
8����I�;Yd��4<~��O�	9���aᅫd�r�$1�t�׹�޾Ӫ���e�B3�g&1����������	���	�1Kse�{iR�jێ=yO����S��Z�3C۵�[,퉙��G�g<��������}l��eh۸3�s�m˒����vUZH]FЦc
Ʒ�*��P�^�����Bf�&��K�E��h؈�۶���44+l Qx<�ع=��Y9���4Ӝ�{A�R� O��%�����B\&:�����;Me�J�b~�E*"/�.��y���{A���7ҫR�h��"Q5�!{j�Ր��=�It�����0��x��5g��'Q�)��!>�c���n)2�_����J�e"<��0W0О⛅���� {Fug�I}�N�ņ�բ��A�rE]`"@��-"�� �p'U�=v�wl����]{�]4^�q~=x�=�p
��39h�����O$�*��ˇ_}~���o~Q�:w�����X/XWU��[.b#q׈�D|h�����}���88�X
� �=b�>�0`�	e�	WZ�Xs�$��f9LE9u��6��@rQ�@EA�s�
���6]�p�+3�g��u���!�l��f�C�Y�H\�'�q�z�K�Ń��>�n��#ɼ�!��h�B��Q��1��s+��K'K��Mv��Os)�]�������T�剰��Ϩ"=��@��Z��o�H0�Ă."��U.$E
`h�f %�O�4��TB�Cx�BY{Hw���^b'iT��e�`1�S�C���TA1x��R­M�=�.m�{_ő�i��W����V��%y��ޛ�|\���[RQ��%�u�W�њ��o�&��l� 󏅴7�ʥU�����gY�eurD�/D� !f��r�⤺&�{!�>^�����Ӥ�3)���-9�AX������q��7�QPB[�C.t�䀣Wl%(J0����Ԕ[��/�������jۂ��W�־��ƾ�F���$�=���-���z�❎��4��%A�T�$ΩvLe��ߤT�
0�Bc������м�����a�m޴���5���}3҆�y��.�	��-2c�7W�k�#�̐��qڀљ�m�f�h��Q��՞�J�3s		m%�>�QT��xX�+ʁcrsKH�\���1��#'a?�j;:����
��v{C��heIMWkz�� ��SzйB�������溔ŷ�ڐ|��&CRq�"]�)��[����u����hb?0#ކB��um�����^�O��K�Ƈ"���Nhl���[)���T�.�T]_<�I���8�ɘ<��u�����5P�/�s����*E����"���T�xJ۳6|_j�,�5�T��-H�2�N(w��Y[�?�H����<�Yk�k�O|�i|���|̢�>㓯t�0{g�E�K��;�x�+�e����6�еf�6�[,]3�at���&�5����J�4k�[b�s�m���S�V����G����ۗC�~&��D�%�3��1#:V�9���zE�p�k�n�R��)4��빣8{�z�6�}�<!e���Ā�3����$�2c����(��x���^�^LC��X�a&��Ȧ,n�"�DO&y�Xlt���:��l��̶r�A멈���FO�O��>�7�0W�[�ݰ��ōG�P/d�y"�$;=�F��˾�y6v�!�6�Yf�Z�1�GP`:sш5�X0˽��r�t�ϓJ�
-�xKV���|�����n�� ���}a
&	�D
�D�\�T7��Kr���m����h7�����>O�>4o���eG=�$��#�ǒ�ؓ�C'��v+���͖�����[����R�FW<GIiR�D����\U��p���ށř�����A&+?�7<��/�y�ؒDՃ��
��W��Ip���{��h?��z�Q(CV����<Oq�v������]t&�?��'�g���)�㫜�%ǰ)[щ�D���⊣�ኆ��^�רo���ׂA_��}BFZ���U�<=*�:�t���8o�l(��J����xT�)�*R@ԁ�E��h�Qη�QT���%�݀K,X�����O�{�8�r�l|\���'~Y��0e[�0A�ً��?�֥�R��?���      ,      x������ � �     